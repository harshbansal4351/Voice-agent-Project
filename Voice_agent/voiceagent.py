import os
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import whisper
from textblob import TextBlob

# --- TWILIO SETUP ---
account_sid = "ACf81ac6547cb6a7e82a8aaf78c4901a0e"
auth_token = "9fe3611c45cb60447435de903ba38fc6"
twilio_from = "+19594569862"
call_to = "+919212314351"

client = Client(account_sid, auth_token)

# --- FLASK SERVER ---
app = Flask(__name__)

@app.route("/voice", methods=["GET", "POST"])
def voice():
    """Bot asks screening question and records answer"""
    resp = VoiceResponse()
    resp.say("Hi. This is an AI recruiter. Please tell us about your experience, skills, and location.", voice='alice')
    resp.record(
        action="/process",
        max_length=30,
        timeout=2,
        play_beep=True
    )
    return str(resp)

@app.route("/process", methods=["GET", "POST"])
def process():
    """Download recording, transcribe, and analyze response"""
    recording_url = request.values["RecordingUrl"] + ".mp3"
    print(f"[🔊] Recording: {recording_url}")
    os.system(f"curl -o response.mp3 {recording_url}")

    # Transcribe with Whisper
    model = whisper.load_model("base")
    result = model.transcribe("response.mp3")
    transcript = result["text"]
    print("[📝] Transcript:", transcript)

    # Analyze tone
    sentiment = TextBlob(transcript).sentiment.polarity
    tone = "positive" if sentiment > 0.1 else "neutral" if sentiment >= -0.1 else "negative"

    # Decision logic
    if "fresher" in transcript.lower() and tone == "positive":
        decision = "You are recommended for the next round."
    elif tone == "negative":
        decision = "We are escalating your profile to human HR."
    else:
        decision = "Thank you. We will get back to you."

    # Respond
    resp = VoiceResponse()
    resp.say(f"Thank you. {decision}", voice='alice')
    resp.hangup()
    return str(resp)

# --- Start Call ---
def start_call():
    print("[📞] Initiating call...")
    call = client.calls.create(
        url="https://eb24-110-235-234-19.ngrok-free.app",  # Will replace this with ngrok when deployed
        to=+919212314351,
        from_=+19594569862
    )
    print("[✅] Call SID:", call.sid)

if __name__ == "__main__":
    import threading
    # Start Flask server in a separate thread
    threading.Thread(target=lambda: app.run(debug=True, use_reloader=False)).start()

    # Delay to let Flask start
    import time
    time.sleep(2)

    # Start the call
    start_call()
