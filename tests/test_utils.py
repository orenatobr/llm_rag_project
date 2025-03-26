from app.utils import load_documents_from_folder


def test_load_documents_from_folder(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("Test content")
    docs = load_documents_from_folder(str(tmp_path))
    assert len(docs) == 1
    assert docs[0] == "Test content"
