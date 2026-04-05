import pickle
import gzip
import warnings
import re
import io
from pathlib import Path

import numpy as np
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import PyPDF2
import docx as python_docx

warnings.filterwarnings("ignore")

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR     = Path(__file__).parent
TFIDF_PATH   = BASE_DIR / "tfidf.pkl"
ENCODER_PATH = BASE_DIR / "encoder.pkl"
MODEL_PATH   = BASE_DIR / "clf.pkl"
INDEX_PATH   = BASE_DIR / "static" / "index.html"

# ── Load models ────────────────────────────────────────────────────────────────
with open(TFIDF_PATH, "rb") as f:
    tfidf = pickle.load(f)

with open(ENCODER_PATH, "rb") as f:
    encoder = pickle.load(f)

with open(MODEL_PATH, "rb") as f:
    classifier = pickle.load(f)

CATEGORIES = encoder.classes_.tolist()
print(f"✅ Models loaded — {len(CATEGORIES)} categories")

# ── App ────────────────────────────────────────────────────────────────────────
app = FastAPI(title="Resume Category Classifier")

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Helpers ────────────────────────────────────────────────────────────────────
def clean_text(text: str) -> str:
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text

def extract_from_pdf(data: bytes) -> str:
    reader = PyPDF2.PdfReader(io.BytesIO(data))
    return " ".join(
        page.extract_text() or "" for page in reader.pages
    )

def extract_from_docx(data: bytes) -> str:
    doc = python_docx.Document(io.BytesIO(data))
    return " ".join(para.text for para in doc.paragraphs)

def predict_text(raw_text: str):
    cleaned = clean_text(raw_text)
    vec     = tfidf.transform([cleaned]).toarray()
    pred    = classifier.predict(vec)[0]
    category = encoder.inverse_transform([pred])[0]
    return category

# ── Routes ─────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
def ui():
    if INDEX_PATH.exists():
        return INDEX_PATH.read_text(encoding="utf-8")
    return "<h2>index.html nahi mila — isko main.py ke saath rakhein.</h2>"


@app.get("/health")
def health():
    return {"status": "ok", "categories": len(CATEGORIES)}


@app.get("/categories")
def get_categories():
    return {"total": len(CATEGORIES), "categories": CATEGORIES}


# ── /predict/file  (HTML ka file upload tab) ──────────────────────────────────
@app.post("/predict/file")
async def predict_file(file: UploadFile = File(...)):
    ext = file.filename.rsplit(".", 1)[-1].lower()
    if ext not in ("pdf", "docx", "txt"):
        raise HTTPException(400, "Sirf PDF, DOCX ya TXT files allowed hain.")

    data = await file.read()

    try:
        if ext == "pdf":
            raw_text = extract_from_pdf(data)
        elif ext == "docx":
            raw_text = extract_from_docx(data)
        else:  # txt
            raw_text = data.decode("utf-8", errors="ignore")
    except Exception as e:
        raise HTTPException(422, f"File parse nahi hui: {e}")

    if len(raw_text.strip()) < 20:
        raise HTTPException(422, "File mein kafi text nahi mila.")

    category = predict_text(raw_text)

    preview = raw_text.strip()[:400].replace("\n", " ")

    return {
        "predicted_category": category,
        "preview": preview,
        "filename": file.filename,
    }


# ── /predict/text  (HTML ka paste text tab) ───────────────────────────────────
class TextInput(BaseModel):
    text: str

@app.post("/predict/text")
def predict_text_endpoint(body: TextInput):
    if len(body.text.strip()) < 20:
        raise HTTPException(400, "Text bahut chhota hai — thoda aur likhein.")

    category = predict_text(body.text)
    return {"predicted_category": category}