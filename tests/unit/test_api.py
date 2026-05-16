from pathlib import Path

from fastapi.testclient import TestClient

from api.main import app


def test_summary_endpoint():
    client = TestClient(app)
    response = client.post("/summary", json={"text": "hello world"})
    assert response.status_code == 200
    assert "summary" in response.json()


def test_convert_not_found():
    client = TestClient(app)
    response = client.post("/convert", json={"source_path": "missing.docx", "target_format": "pdf"})
    assert response.status_code == 404


def test_merge(tmp_path: Path):
    a = tmp_path / "a.txt"
    b = tmp_path / "b.txt"
    a.write_text("a")
    b.write_text("b")
    client = TestClient(app)
    response = client.post("/merge", json={"source_paths": [str(a), str(b)]})
    assert response.status_code == 200
