from app.rag_pipeline import build_rag_pipeline
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)


def main():
    """
    Main function that runs the RAG pipeline and allows user input.
    """
    folder_path = "data/sample_docs"
    qa_pipeline = build_rag_pipeline(folder_path)

    logger.info("Local RAG System with Mistral (via Ollama). Type 'exit' to quit.")
    while True:
        query = input("\nQuestion: ")
        if query.lower() == "exit":
            break
        response = qa_pipeline.invoke(query)
        logger.info("Answer:\n%s", str(response["result"]).strip())


if __name__ == "__main__":
    main()
