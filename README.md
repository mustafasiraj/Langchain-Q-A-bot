# 📄 LangChain PDF Q&A Bot (Terminal Version)
- **This is a terminal-based Python application that lets you:**

**Load one or more PDF files.**

**Ask any question based on the content of the PDFs.**

**Get answers powered by LangChain and OpenAI.**

**See source snippets from your PDFs used to generate the answers.**

---------

## 🚀 Features
**📎 Upload multiple PDFs from local file paths**

**🤖 Use OpenAI LLM for answering questions**

**📚 Returns top content snippets as evidence**

**🧠 Memory-efficient (uses FAISS for fast vector search)**

**🧪 Runs completely in terminal — no Streamlit or web UI**

------------

## 🛠️ Dependencies
**Install required packages:**

- pip install langchain openai faiss-cpu pypdf tiktoken

----------------

## 🧾 How to Use
- Clone or copy this script into a .py file (e.g. pdf_qa_bot.py)

- Make sure you set your OpenAI API key:

- Option 1: Directly in the script (in os.environ["OPENAI_API_KEY"])

- Option 2: Use a .env file and load it via dotenv (optional)

- Run the script:

- python pdf_qa_bot.py
- When prompted:

- Enter one or more full file paths to your PDF(s) like:

- H:\PDFs\intro_to_Machine_learning_Test.pdf
- Then type your question about the content.

------------

## 📦 File Structure Example

|pdf_qa_bot.py        |    ← Your main Python script|
|README.md            |    ← (This file)            |
|H:\PDFs\yourfile.pdf | ← PDF file path you enter   |

🧠 How It Works
Loads PDFs using PyPDFLoader.

Splits them into chunks using CharacterTextSplitter.

Embeds the chunks using OpenAIEmbeddings.

Stores and indexes them with FAISS.

When a question is asked:

It retrieves relevant chunks

Passes them to RetrievalQA using OpenAI

Returns the answer and shows preview snippets from top matched content.

------------

🔐 API Key Warning
Never commit your OPENAI_API_KEY to public GitHub repositories.

Use .env or other secret management practices.

----------------

🧪 Example Output

## 📄 LangChain PDF Q&A Bot (Terminal Version)
**Enter path(s) to PDF file(s), separated by commas:
> H:\PDFs\intro_to_Machine_learning_Test.pdf

----------

## ❓ What do you want to ask about your PDFs?
> What is this PDF about?

-------------

#### ⏳ Processing your PDFs and question...

**✅ Answer:
This PDF is about the fundamentals of machine learning, including its types and how it works.**

### 📚 Top Source Snippets:

**Source 1:
Machine learning is a subset of AI that enables systems to learn and improve...**

**Source 2:
There are three types of learning: supervised, unsupervised, and reinforcement...**
