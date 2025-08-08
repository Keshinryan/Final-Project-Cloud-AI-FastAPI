# Cloud AI API - Animal Taxonomy Classification (FastAPI)

This is the cloud deployment module of the Final Project titled **"Design of Animal Classification System Using Deep Learning on Android"**, focusing on image-based animal taxonomy classification using a deep learning model deployed via **FastAPI**.

## 🧠 Project Overview

This API classifies animal images into five levels of biological taxonomy: `Kelas`, `Ordo`, `Famili`, `Genus`, and `Spesies`.

It supports multiple TensorFlow/Keras models, including:
- `D3(4HL+0.2D).h5`: Best performance model
- `M3(4HL+0.2D).h5`: Edge AI compatible version

## 🚀 Other Repositories

This AI Deployment is integrated into different platforms through separate repositories:

- **Model Training**  
  [Final-Project-Model-Training](https://github.com/Keshinryan/Final-Project-Model-Training)

- **Cloud Deployment (Gradio + Vercel + Express.js)**  
  [Final-Project-Cloud-AI-Gradio-VercelJs-ExpressJs](https://github.com/Keshinryan/Final-Project-Cloud-AI-Gradio-VercelJs-ExpressJs)

- **Mobile Application**  
  [Final-Project-Mobile-TaxoClassify](https://github.com/Keshinryan/Final-Project-Mobile-TaxoClassify)

## 🔧 Tech Stack

- **Framework**: FastAPI
- **Model Format**: Keras `.h5`
- **Deployment**: Hugging Face Spaces (via Docker container)
- **Inference**: Multi-output, multi-class classification

## 📁 File Descriptions

| File                        | Description |
|-----------------------------|-------------|
| `app.py`                   | Main FastAPI app for model inference |
| `D3(4HL+0.2D).h5`          | Deep Learning model file (best version) |
| `M3(4HL+0.2D).h5`          | Alternate model for deployment |
| `label_encodings.json`     | Label encodings for taxonomy levels |
| `label_encodings2.json`    | Backup or alternative label encoding |
| `Dockerfile`               | Docker configuration for Hugging Face |
| `requirements.txt`         | Python dependencies |
| `README.md`                | This file |

## 🚀 Deployment Instructions

### Run Locally
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

### Deploy to Hugging Face (Docker-based Space)
1. Create a new Space with Docker template.
2. Upload all files in this folder.
3. Make sure the Dockerfile exposes port 7860 and runs `uvicorn app:app --host 0.0.0.0 --port 7860`.

## 🔄 API Endpoint

**POST** `/predict`

**Form-data**:
- `file`: image file (.jpg/.png)

**Response**:
```json
{
  "predictions": {
    "kelas": "Aves",
    "ordo": "Passeriformes",
    "famili": "Passeridae",
    "genus": "Passer",
    "spesies": "Passer montanus"
  }
}
```

## 📚 Use Case

Used by the Android application to perform cloud inference when internet connection is available. Aims to assist users in learning biodiversity and taxonomy through real-time image classification.

---
Final Project — Informatics Engineering — 2025
