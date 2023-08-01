import os
import pandas as pd
from flask import Flask, jsonify, request
from audio_processing import extract_features
from model import train_classifier, load_classifier, predict_genre

app = Flask(__name__)

data_path = 'path/to/audio_data'

#endpoint to handle audio file upload
@app.route('/api/predict', methods=['POST'])
def predict_audio_genre():
    if 'audio' not in request.files:
        return jsonify(error='No audio file'), 400
    
    audio_file = request.files['audio']
    if audio_file.filename == '':
        return jsonify(error= 'No selected audio file'), 400
    
    audio_features = extract_features(audio_file)
    predicted_genre = predict_genre(audio_features)
    
    return jsonify(predictedGenre=predicted_genre)

if __name__ == '__main__':
    app.run(debug=True)