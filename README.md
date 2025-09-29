🩺 Lung Cancer Detection System
📌 Overview

This project is a Deep Learning-based Lung Cancer Detection System that helps identify lung cancer from CT/X-ray scans. The system uses a trained model (best_model.h5) to classify scans and provides predictions with confidence scores through a simple and interactive web interface.

🔗 Project Files: https://drive.google.com/drive/folders/1I0JPULp_pMPGD2XcBfTzVyr4vM53DSYu?usp=sharing

⚙️ Features

🧠 Deep Learning Model trained with TensorFlow/Keras.

🌐 Web Interface built using HTML, CSS, and JavaScript.

📂 Upload & Preview CT/X-ray scans.

⚡ Real-time Predictions via Flask backend.

📱 Responsive UI with gradient design, icons, and loading spinner.

🛠️ Tech Stack

Model: TensorFlow/Keras (best_model.h5)

Backend: Flask API (Python)

Frontend: HTML, CSS, JavaScript

🚀 How It Works

User uploads a CT/X-ray scan.

The image is sent to the Flask backend.

The trained deep learning model predicts the class (cancerous or non-cancerous).

Results are displayed with prediction label and confidence score.

📂 Repository Structure
.
├── index.html        # Frontend UI for uploading & prediction
├── TODO.md           # Enhancement plan for UI
├── best_model.h5     # Trained deep learning model
└── app.py (planned)  # Flask backend for predictions

📌 Future Enhancements

☁️ Deploy on cloud platforms (Heroku/AWS).

📊 Multi-class classification (benign vs malignant).

🖼️ Visualization with Grad-CAM for explainability.

🔒 Secure patient data handling.
