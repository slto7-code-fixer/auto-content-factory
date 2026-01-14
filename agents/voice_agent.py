def generate_voice(text):
    with open("voice.txt", "w", encoding="utf-8") as f:
        f.write(text)
    return "voice.txt"
