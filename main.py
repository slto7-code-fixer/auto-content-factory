import traceback

try:
    # كل كودك هنا
    from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
    import os, random

    print("📌 Starting video generation...")

    # اختيار الصور
    image_folder = "images"
    if not os.path.exists(image_folder):
        raise Exception(f"Folder '{image_folder}' not found!")

    images = os.listdir(image_folder)
    if len(images) < 1:
        raise Exception("No images found in the folder!")

    print(f"Found {len(images)} images, selecting...")

    selected_images = random.sample(images, min(3, len(images)))
    clips = [ImageClip(os.path.join(image_folder, img)).set_duration(5) for img in selected_images]

    video = concatenate_videoclips(clips, method="compose")

    # إضافة الصوت
    audio_path = "voice.mp3"
    if os.path.exists(audio_path):
        print("Voice found, adding to video...")
        audio = AudioFileClip(audio_path)
        video = video.set_audio(audio)
    else:
        print("⚠️ Voice not found, skipping audio.")

    # تصدير الفيديو
    output_file = "final_video.mp4"
    video.write_videofile(output_file, fps=24)
    print(f"✅ Video created: {output_file}")

except Exception as e:
    print("❌ ERROR occurred:")
    traceback.print_exc()
    raise
