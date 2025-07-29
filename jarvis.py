import openai
import requests
import os
import tempfile
import random
import pygame
import speech_recognition as sr

# === 🔐 API KEYS ===
openai.api_key = "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"
ELEVENLABS_API_KEY = "sk_8d91639a929dfc2da5b6ead46801d4d7b2905b80c04855ac"
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"




# === 🎤 Listen from user ===
def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening... Speak your question.")
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio, language='hi-IN')
        print(f"🗣️ You said: {query}")
        return query
    except sr.UnknownValueError:
        return "माफ़ कीजिए, मैं समझ नहीं पाया।"
    except sr.RequestError:
        return "Network error occurred while listening."

# === 🧠 GPT Teacher Response ===
def get_gpt_response(prompt):
    print("🧠 Thinking like a teacher...")
    system_behavior = random.choice([
        "You are a calm and helpful teacher who gives polite and friendly answers in Hindi-English mix.",
        "You are a senior professor guiding students clearly with simple language.",
        "You are a young tech-savvy teacher who interacts playfully with students, using basic Hindi and English."
    ])

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_behavior},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# === 🔊 Speak the reply using ElevenLabs ===
def speak(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.8
        }
    }

    print("🗣️ Speaking like a teacher...")
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            fp.write(response.content)
            temp_path = fp.name

        pygame.mixer.init()
        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        os.remove(temp_path)
    else:
        print("🔴 Error with ElevenLabs:", response.text)

# === 🎓 Greeting message ===
def greet_student():
    intro = "Hello students! मैं JARVIS, आपका स्मार्ट क्लासरूम असिस्टेंट हूँ। आप मुझसे कोई भी सवाल पूछ सकते हैं, चलिए शुरू करते हैं।"
    print("👋", intro)
    speak(intro)

# === 🔁 Main Loop ===
if __name__ == "__main__":
    print("🎓 Welcome to JARVIS Teacher Assistant")
    greet_student()

    while True:
        question = listen_to_user()
        if question.lower() in ["exit", "quit", "bye", "close"]:
            speak("ठीक है, अलविदा! मिलते हैं फिर से।")
            break
        reply = get_gpt_response(question)
        print("🧑‍🏫 JARVIS Reply:", reply)
        speak(reply)
