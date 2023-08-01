import librosa

def extract_features(audio_file):
    audio_path = 'uploaded_audio.wav'
    audio_file.save(audio_path)
    
    #extract audio features (MFCCs)
    y, sr = librosa.load(audio_path)
    mfccs = librosa.feature.mfcc(y=y, sr=sr)
    
    #delete the temp audio file
    os.remove(audio_path)
    
    return mfccs