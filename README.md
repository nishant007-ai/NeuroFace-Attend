# 🤖 NeuroFace-Attend 🎙️  
**AI/ML-Powered Face Recognition + Voice-Assisted Attendance System**  

![Python](https://img.shields.io/badge/Python-3.9+-blue)  
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-orange)  
![AI/ML](https://img.shields.io/badge/AI%2FML-Face_Recognition-green)  
![Voice Assistant](https://img.shields.io/badge/Feature-Voice_Assistant-purple)  
![License](https://img.shields.io/badge/License-MIT-red)  

---

## 🌐 Live Demo  
🎉 Check it out live here: **[NeuroFace-Attend on Render](https://neuroface-attend-3.onrender.com)**  

---

## 🌟 What is NeuroFace-Attend?  
**NeuroFace-Attend** is a **smart attendance system** that combines **AI-based face recognition** with an **interactive voice assistant**. It makes attendance tracking **fast, accurate, and interactive** for schools, offices, hospitals, or factories.  

**Who can use it:**  
- 🏫 Schools & Colleges  
- 🏢 Corporate Offices & Startups  
- 🏥 Hospitals  
- 🏬 Malls & Enterprises  
- 🏭 Factories & Industries  
- 🏛️ Government & Military Institutions  

---

## 🚀 Key Features  

- 🔹 **AI-Powered Face Recognition** – Ultra-fast and highly accurate (99%+).  
- 🔹 **Voice Assistant Integration** – Greets users, confirms attendance, and guides fine payments.  
- 🔹 **Duplicate Prevention** – Each person can mark attendance **only once per session**.  
- 🔹 **Real-Time Notifications** – Instant voice & visual feedback after marking attendance.  
- 🔹 **Fine Clearance System** – Automatically calculates fines for absentees; upload payment proof.  
- 🔹 **Voice-Controlled History Search** – Query by **Name, Roll, or Subject** using your voice.  
- 🔹 **Cross-Platform** – Works on **Web, Desktop, Raspberry Pi, and Kiosk devices**.  

---

## 🖼️ How It Works  

1️⃣ **Voice-Guided Face Registration** – Assistant guides users during registration.  
2️⃣ **AI Recognition** – Scans and matches faces in milliseconds.  
3️⃣ **Voice Feedback** – Assistant speaks messages like:  
   - `"Hello Tony! Your attendance for OOMD has been marked ✅"`  
   - `"You have already marked attendance today ❌"`  
4️⃣ **Detailed Reporting** – Filter by **Subject, Date, Department** using **voice or text** commands.  
5️⃣ **Fine Clearance** – Voice-guided fine payment with QR code and digital proof upload.  

---

## 🔧 Tech Stack  

- **Frontend:** Streamlit  
- **Face Recognition:** dlib + face_recognition  
- **Voice Assistant:** pyttsx3 (TTS) + SpeechRecognition (STT)  
- **Data Management:** Pandas (CSV) or SQLite (upgradable to MySQL/Postgres)  
- **AI Models:** Deep CNN embeddings for facial features  

---

## 🎤 Voice Assistant Demo Commands  

- **Attendance:** `"Hey NeuroFace, mark my attendance"`  
- **History Search:** `"Show me OOMD attendance for Tony"`  
- **Fine Clearance:** `"Do I have any pending fines?"`  

Assistant replies using **Text-to-Speech (TTS)** and can support **multiple languages 🌍**.

---

## 🖥️ Installation (Local Setup)  

```bash
# 1️⃣ Clone the Repository
git clone https://github.com/nishant007-ai/NeuroFace-Attend.git
cd NeuroFace-Attend

# 2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3️⃣ Install Requirements
pip install -r requirements.txt

# 4️⃣ Run the App
streamlit run app.py
