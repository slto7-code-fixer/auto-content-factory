def generate_video(script, voice):
    with open("video.txt", "w", encoding="utf-8") as f:
        f.write("VIDEO READY\n")
        f.write(script)
    return "video.txt"
