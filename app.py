from fastapi import FastAPI, File, UploadFile # type: ignore
import numpy as np
import tensorflow as tf # type: ignore
from tensorflow.keras.preprocessing.image import img_to_array # type: ignore
from PIL import Image
import io
import json

app = FastAPI()

# Load the trained multi-output model
model = tf.keras.models.load_model("D3(4HL+0.2D).h5", compile=False)

# Load label encodings from JSON
with open("label_encodings2.json", "r") as f:
    label_encodings = json.load(f)

# Reverse the encodings to map index back to label
reverse_label_encodings = {
    label: {int(v): k for k, v in encodings.items()}
    for label, encodings in label_encodings.items()
}

# Order of the taxonomy outputs
taxonomy_labels = ["kelas", "ordo", "famili", "genus", "spesies"]

# Preprocess input image
def preprocess_image(image):
    image = image.resize((256, 256))  # Match your model input
    image = img_to_array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.get("/")
async def root():
    return {"message": "Taxonomy classification API is running"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        # Read and preprocess image
        image = Image.open(io.BytesIO(await file.read())).convert("RGB")
        processed_image = preprocess_image(image)

        # Predict using the model
        predictions = model.predict(processed_image)

        # Format results
        predicted_labels = {}
        for i, label in enumerate(taxonomy_labels):
            pred_probs = predictions[i][0]
            pred_index = np.argmax(pred_probs)
            confidence = float(pred_probs[pred_index])
            predicted_label = reverse_label_encodings[label][pred_index]
            predicted_labels[label] = {"label": predicted_label, "confidence": confidence}

        return predicted_labels
    except Exception as e:
        return {"error": str(e)}
