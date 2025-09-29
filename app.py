from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np
import os

# Load your trained model
model_path = "best_model.h5"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found at {model_path}")

model = load_model(model_path)

# Define class labels manually (same as used in training)
class_labels = ['Benign cases', 'Malignant cases', 'Normal cases']

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    try:
        img_file = request.files["file"]
        img_file.stream.seek(0)
        img = Image.open(img_file.stream)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img = img.resize((224, 224))
        img_array = np.expand_dims(image.img_to_array(img)/255.0, axis=0)

        pred = model.predict(img_array)
        pred_idx = np.argmax(pred, axis=1)[0]
        confidence = float(np.max(pred))

        return jsonify({"class": class_labels[pred_idx], "confidence": confidence})
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

