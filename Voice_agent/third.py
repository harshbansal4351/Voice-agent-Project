import whisper
from textblob import TextBlob
import re

# STEP 1: Transcribe the audio using Whisper
print("🔁 Loading Whisper model...")
model = whisper.load_model("base")

audio_file = "voice_ai_agent_sample.mp3"  # Make sure this file is in the same folder

print("🎧 Transcribing audio...")
result = model.transcribe(audio_file)
transcript = result["text"]
print("\n📝 Transcript:")
print(transcript)

# STEP 2: Extract keywords
def extract_keywords(text):
    name = re.findall(r"I[’']?m ([A-Z][a-z]+ [A-Z][a-z]+)", text)
    skills = re.findall(r"proficient in (.+?)\.", text)
    location = re.findall(r"I live in ([A-Za-z]+)", text)
    is_fresher = "fresher" in text.lower()

    return {
        "Name": name[0] if name else "Not found",
        "Skills": skills[0].split(", ") if skills else [],
        "Location": location[0] if location else "Not mentioned",
        "Experience": "Fresher" if is_fresher else "Experienced"
    }

# STEP 3: Analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return "Positive" if polarity > 0.1 else "Neutral" if polarity >= -0.1 else "Negative"

# STEP 4: Decision logic
def agent_decision(info, sentiment):
    if info["Experience"] == "Fresher" and sentiment == "Positive":
        return "Recommend for next round"
    elif sentiment == "Negative":
        return "Escalate to human HR for review"
    else:
        return "Put on hold"

# Run analysis
keywords = extract_keywords(transcript)
sentiment = analyze_sentiment(transcript)
recommendation = agent_decision(keywords, sentiment)

# Final Output
print("\n🔍 Extracted Info:")
for k, v in keywords.items():
    print(f"{k}: {v}")

print(f"\n🧠 Sentiment: {sentiment}")
print(f"✅ Recommendation: {recommendation}")