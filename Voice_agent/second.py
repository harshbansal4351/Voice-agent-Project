import whisper

# Load the Whisper model (choose: tiny, base, small, medium, large)
model = whisper.load_model("base")

# Path to your audio file
audio_file = "voice_ai_agent_sample.mp3"

# Transcribe the audio
result = model.transcribe(audio_file)

# Print the transcription
print("🔊 Transcribed Text:")
print(result["text"])
