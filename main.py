import os
import tempfile
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Set your API key here (or use .env file or prompt)
os.environ["OPENAI_API_KEY"] = "sk-your-real-key-here"

def load_pdf_and_create_qa(pdf_paths):
    all_pages = []

    for path in pdf_paths:
        loader = PyPDFLoader(path)
        all_pages.extend(loader.load())

    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(all_pages)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)

    retriever = vectorstore.as_retriever()
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),
        retriever=retriever,
        return_source_documents=True
    )

    sources = [doc.page_content[:300].strip() + "..." for doc in chunks[:3]]
    return qa, sources

def main():
    print("📄 LangChain PDF Q&A Bot (Terminal Version)")

    # Step 1: Ask for PDF file paths
    paths_input = input("Enter path(s) to PDF file(s), separated by commas:\n> ")
    pdf_paths = [p.strip() for p in paths_input.split(",") if p.strip()]

    # Step 2: Ask a question
    question = input("\n❓ What do you want to ask about your PDFs?\n> ")

    if not pdf_paths or not question:
        print("❌ Please provide both PDF paths and a question.")
        return

    print("\n⏳ Processing your PDFs and question...\n")

    try:
        qa, sources = load_pdf_and_create_qa(pdf_paths)
        result = qa.invoke({"query": question})
        answer = result["result"]

        print("✅ Answer:")
        print(answer)
        print("\n📚 Top Source Snippets:")
        for i, source in enumerate(sources, 1):
            print(f"\nSource {i}:\n{source}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
