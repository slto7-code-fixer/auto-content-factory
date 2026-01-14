# main.py
from agents.voice_agent import generate_voice

def main():
    # مثال على نص عربي
    script = """
    السلام عليكم ورحمة الله وبركاته.
    هذا اختبار لصوت عربي باستخدام gTTS.
    يمكن تعديل النص أو اللغة لأي مشروع محتوى تلقائي.
    """
    
    # توليد الصوت
    voice_file = generate_voice(script)
    print("✅ تم توليد الملف الصوتي:", voice_file)

if __name__ == "__main__":
    main()
