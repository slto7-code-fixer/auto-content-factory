# agents/voice_agent.py
from gtts import gTTS

def generate_voice(text, lang="ar"):
    """
    توليد ملف صوتي من النص.
    - text: النص المراد تحويله لصوت
    - lang: اللغة ('ar' عربي، 'en' إنجليزي، 'fr' فرنسي...)
    """
    output_file = "voice.mp3"
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)
    return output_file
