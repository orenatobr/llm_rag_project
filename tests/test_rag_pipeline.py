from tests.fakes import FakeLLM, FakeEmbeddings
from app.utils import load_documents_from_folder
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain.chains import RetrievalQA


def test_rag_pipeline_build():
    docs_raw = load_documents_from_folder("data/sample_docs")
    docs = [Document(page_content=doc) for doc in docs_raw]
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)

    embeddings = FakeEmbeddings()
    vectordb = FAISS.from_documents(split_docs, embeddings)
    retriever = vectordb.as_retriever()

    qa = RetrievalQA.from_chain_type(llm=FakeLLM(), retriever=retriever)
    result = qa.invoke("Test question")
    assert result["result"] == "mocked result"
