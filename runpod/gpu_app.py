
import joblib
from pathlib import Path

import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification

import os

MODEL_DIR = Path(
    os.environ.get(
        "MODEL_DIR",
        "/workspace/models/distilbert_resume_classifier_v2"
    )
)

app = FastAPI(title="KnZ Resume Classification API")

tokenizer = AutoTokenizer.from_pretrained(str(MODEL_DIR))
model = AutoModelForSequenceClassification.from_pretrained(str(MODEL_DIR))

label_encoder = joblib.load(MODEL_DIR / "label_encoder.pkl")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()


class ResumeRequest(BaseModel):
    text: str


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "KnZ resume classifier",
        "device": str(device),
        "model_loaded": True,
    }


@app.post("/predict")
def predict(request: ResumeRequest):
    text = request.text.strip()

    if not text:
        raise HTTPException(status_code=400, detail="Resume text cannot be empty.")

    inputs = tokenizer(
        text,
        truncation=True,
        padding=True,
        max_length=512,
        return_tensors="pt",
    )
    inputs = {key: value.to(device) for key, value in inputs.items()}

    with torch.inference_mode():
        outputs = model(**inputs)
        probabilities = torch.softmax(outputs.logits, dim=-1)[0]
        predicted_id = int(torch.argmax(probabilities).item())
        confidence = float(probabilities[predicted_id].item())

    predicted_label = str(label_encoder.inverse_transform([predicted_id])[0])

    return {
        "predicted_class": predicted_label,
        "class_id": predicted_id,
        "confidence": confidence,
    }
