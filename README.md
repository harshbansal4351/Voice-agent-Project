🎙️ Voice AI Agent for Candidate Screening

This project simulates a Voice AI agent that automates the initial telephonic screening of job candidates. It transcribes an audio call, extracts relevant candidate information, analyzes sentiment, and recommends actions (proceed, escalate, or hold) based on the responses.

---

🚀 Features

- 🎧 Audio Transcription using OpenAI Whisper (offline or API)
- 🧠 Sentiment Analysis with TextBlob
- 🔍 Information Extraction: Name, Skills, Location, Experience
- 🤖 Agent Decision Logic: Recommends next steps based on tone and experience
- 🖼️ Includes flowchart, one-pager, and sample output card

---

📂 Project Structure

voice-ai-agent/
├── voice_ai_agent.py           # Main script
├── voice_ai_agent_sample.mp3   # Sample audio file
├── AgentFlowchart.png          # Reasoning flow diagram
├── OutputCard.png              # UI-style result card
├── OnePager.pdf                # Project summary
└── README.md                   # This file

---

📌 Requirements

- Python 3.8+
- Git
- pip packages:
  - whisper
  - torch
  - textblob
- ffmpeg (installed separately)

---

⚙️ Installation

# Clone the repo
git clone https://github.com/yourusername/voice-ai-agent.git
cd voice-ai-agent

# Install Python dependencies
pip install git+https://github.com/openai/whisper.git
pip install torch textblob

# One-time TextBlob corpus download
python -m textblob.download_corpora

---

▶️ How to Run

1. Place your MP3 audio in the folder (name it voice_ai_agent_sample.mp3)
2. Run the script:
   python voice_ai_agent.py
3. You’ll get:
   - Transcript
   - Extracted info
   - Sentiment
   - Final recommendation

---

🧠 Agent Decision Flow

The agent decides based on:
- Experience (Fresher/Experienced)
- Sentiment (Positive/Neutral/Negative)

Logic:
- If Fresher + Positive        → Recommend for Next Round
- If Negative tone             → Escalate to HR
- If Neutral/Experienced       → Put on Hold

---

📝 Tools Used

- OpenAI Whisper for speech-to-text
- TextBlob for sentiment analysis
- Python for logic & reasoning
- Draw.io / Canva for visualization

---

📄 License

This project is licensed under the MIT License.

---

👨‍💻 Author

Harsh Bansal  
LinkedIn: https://www.linkedin.com/in/haarshbansal  
Email: bansalharsh500@gmail.com
