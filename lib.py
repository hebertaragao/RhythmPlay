import librosa
def detectar_ritmo(caminho_audio):
    y, sr = librosa.load(caminho_audio)
    tempo, _= librosa.beat.beat_track(y=y, sr=sr)

    # Aqui você pode melhorar a detecção com machine learning, mas pra agora:
    if tempo < 90:
        ritmo = "Pagode"
    elif tempo < 110:
        ritmo = "Forró"
    elif tempo < 130:
        ritmo = "Axé"
    else:
        ritmo = "Outro"

    return ritmo, round(tempo)
