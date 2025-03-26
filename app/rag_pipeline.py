from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOllama
from app.utils import load_documents_from_folder

from dotenv import load_dotenv

load_dotenv()


def build_rag_pipeline(folder_path: str):
    """
    Builds the RAG pipeline using Ollama (Mistral/LLaMA2): loads documents, creates embeddings, and returns QA chain.

    Args:
        folder_path (str): Path to the .txt documents

    Returns:
        RetrievalQA: Retrieval-based question-answering pipeline
    """
    documents = load_documents_from_folder(folder_path)
    docs = [Document(page_content=doc) for doc in documents]

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="mistral")  # or "llama2"
    vectordb = FAISS.from_documents(split_docs, embeddings)

    retriever = vectordb.as_retriever()
    llm = ChatOllama(model="mistral", temperature=0)

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa
