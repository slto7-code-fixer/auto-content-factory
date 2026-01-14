from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import os, random

# اختيار الصور
image_folder = "images"
images = os.listdir(image_folder)
if len(images) < 1:
    raise Exception("لا توجد صور في المجلد!")

selected_images = random.sample(images, min(3, len(images)))
clips = [ImageClip(os.path.join(image_folder, img)).set_duration(5) for img in selected_images]

video = concatenate_videoclips(clips, method="compose")

# إضافة الصوت
audio_path = "voice.mp3"
if os.path.exists(audio_path):
    audio = AudioFileClip(audio_path)
    video = video.set_audio(audio)

# تصدير الفيديو
video.write_videofile("final_video.mp4", fps=24)
