from agents.idea_agent import get_idea
from agents.script_agent import generate_script
from agents.voice_agent import generate_voice
from agents.video_agent import generate_video

idea = get_idea()
script = generate_script(idea)
voice = generate_voice(script)
video = generate_video(script, voice)

print("VOICE GENERATED")
