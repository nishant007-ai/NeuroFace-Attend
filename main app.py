# Full Advanced JARVIS-Style Voice Assistant (Core Only, No Interface)
# Requirements:
# pip install openai elevenlabs speechrecognition pyaudio

import openai
import speech_recognition as sr
import os
from elevenlabs import generate, play, set_api_key
import pandas as pd

# --- CONFIGURE YOUR API KEYS ---
openai.api_key = "your-openai-api-key"
set_api_key("your-elevenlabs-api-key")

# --- LOAD STUDENT DATA ---
STUDENT_CSV_PATH = "student_data.csv"  # Path to CSV

def load_student_data():
    if os.path.exists(STUDENT_CSV_PATH):
        return pd.read_csv(STUDENT_CSV_PATH)
    else:
        return pd.DataFrame(columns=["Name", "Roll", "Attendance", "Fine"])

students = load_student_data()

# --- FUNCTION TO CONVERT TEXT TO SPEECH ---
def speak(text, voice="Bella"):
    audio = generate(text=text, voice=voice, model="eleven_monolingual_v1")
    play(audio)

# --- FUNCTION TO HANDLE GPT ---
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a kind and smart teacher in a smart classroom."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# --- FUNCTION TO LISTEN VIA MIC ---
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=5)
        try:
            query = recognizer.recognize_google(audio, language="en-IN")
            return query
        except Exception:
            return "Sorry, I couldn't understand."

# --- CORE LOOP ---
print("\n🤖 JARVIS Voice Assistant is running. Ask me anything...")
while True:
    question = listen()
    print(f"You asked: {question}")

    if "attendance of" in question.lower():
        name = question.split("of")[-1].strip().title()
        record = students[students["Name"].str.contains(name, case=False)]
        if not record.empty:
            info = record.iloc[0]
            answer = f"{info['Name']} has {info['Attendance']} percent attendance and rupees {info['Fine']} fine."
        else:
            answer = "I could not find that student's data."
    else:
        answer = ask_gpt(question)

    print(f"JARVIS: {answer}")
    speak(answer)
