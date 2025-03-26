def load_documents_from_folder(folder_path: str) -> list:
    """
    Loads all .txt files from a directory as strings.

    Args:
        folder_path (str): Path to the folder containing .txt files

    Returns:
        list: List of strings with the content of each document
    """
    import os

    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(
                os.path.join(folder_path, filename), "r", encoding="utf-8"
            ) as file:
                documents.append(file.read())
    return documents
