import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("🎤 Listening... Please say something.")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("✅ You said:", text)
except Exception as e:
    print("❌ Error:", e)

