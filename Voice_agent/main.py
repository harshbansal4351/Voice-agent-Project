from gtts import gTTS

script = """
Hello, I’m calling from XYZ company. Could you please introduce yourself?
Hi, I’m Harsh Bansal. I’ve recently completed my B.Tech in Computer Science and I’m passionate about working in the tech industry.
Great! Can you tell me about your key skills?
Sure. I’m proficient in Python, Django, and ReactJS. I’ve also worked with SQL databases.
Do you have any experience?
No, I am a fresher. But I have worked on several academic and personal projects during my college.
Where are you currently located?
I live in Delhi.
Are you available to join within 15 days if selected?
Yes, I’m open to immediate joining.
Perfect. Thank you for your time.
"""

tts = gTTS(text=script, lang='en')
tts.save("voice_ai_agent_sample.mp3")
