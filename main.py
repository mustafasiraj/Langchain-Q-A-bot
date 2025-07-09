import os
import sys
import streamlit as st

# ✅ Ensure local modules folder is in path
sys.path.append(os.path.dirname(__file__))

# ✅ Import your QA chain from modules
from modules.qa_chain import load_pdf_and_create_qa

# ✅ Set your OpenAI key securely
os.environ["OPENAI_API_KEY"] = "ADD_YOUR_OWN_API_KEYYY"

# ✅ Streamlit config
st.set_page_config(page_title="📄 LangChain PDF Q&A Bot", page_icon="🤖")
st.title("📄 LangChain PDF Q&A AI Agent")

# ✅ Session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

# ✅ Upload PDF files
uploaded_files = st.file_uploader("Upload one or more PDF files", type="pdf", accept_multiple_files=True)

# ✅ LLM Backend choice (future expansion)
llm_choice = st.selectbox("Choose LLM Backend", ["OpenAI"])

# ✅ Ask a question
question = st.text_input("Ask a question about your PDFs")

# ✅ Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.history = []
    st.experimental_rerun()

# ✅ Process the question and show the answer
if uploaded_files and question:
    with st.spinner("Processing... Please wait."):
        try:
            qa, sources = load_pdf_and_create_qa(uploaded_files, llm_choice)
            response = qa({"query": question})
            answer = response["result"]
            sources = response.get("source_documents", [])
            st.session_state.history.append((question, answer, sources))
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# ✅ Display chat history
if st.session_state.history:
    st.subheader("🧠 Q&A History")
    for q, a, sources in reversed(st.session_state.history):
        st.markdown(f"**Q:** {q}")
        st.markdown(f"**A:** {a}")
        if sources:
            with st.expander("📚 Sources"):
                for i, s in enumerate(sources, 1):
                    st.markdown(f"**Source {i}:** {s}")
        st.markdown("---")
