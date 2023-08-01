import random

def predict_genre(audio_features):
    genres = ['Rock', 'Pop', 'Hip-Hop', 'Jazz', 'Electronic']
    predict_genre = random.choice(genres)
    
    return predict_genre