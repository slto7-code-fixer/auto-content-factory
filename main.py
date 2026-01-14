from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import random, os

# اختيار صور عشوائية
image_folder = "images"
images = random.sample(os.listdir(image_folder), 3)  # 3 صور عشوائية
clips = [ImageClip(os.path.join(image_folder, img)).set_duration(5).fadein(1).fadeout(1) for img in images]

video = concatenate_videoclips(clips, method="compose")

# إضافة الصوت
audio = AudioFileClip("voice.mp3")
video = video.set_audio(audio)

video.write_videofile("final_video.mp4", fps=24)
