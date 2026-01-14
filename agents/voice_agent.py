import subprocess

def generate_voice(text):
    output = "voice.wav"
    subprocess.run([
        "espeak",
        "-v", "ar",
        "-s", "140",
        "-w", output,
        text
    ])
    return output
