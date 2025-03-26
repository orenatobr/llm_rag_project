def test_rag_pipeline_build():
    from app.rag_pipeline import build_rag_pipeline

    try:
        qa = build_rag_pipeline("data/sample_docs")
        assert qa is not None
    except Exception as e:
        assert False, f"Pipeline build failed: {e}"
