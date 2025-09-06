# 🤖 NeuroFace-Attend 🎙️ – AI/ML Face Recognition + Voice-Assisted Attendance System  

![Python](https://img.shields.io/badge/Python-3.9+-blue)  
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-orange)  
![AI/ML](https://img.shields.io/badge/AI%2FML-Face_Recognition-green)  
![Voice Assistant](https://img.shields.io/badge/Feature-Voice_Assistant-purple)  
![License](https://img.shields.io/badge/License-MIT-red)  

---

## 🌟 **What is NeuroFace-Attend?**

**NeuroFace-Attend** is a next-generation, **AI + Machine Learning-powered Face Recognition Attendance System** with an integrated **Voice Assistant 🤖🔊** that talks back to users during attendance.  

It is built for **all environments**:  
🏫 **Schools & Colleges**  
🏢 **Corporate Offices & Startups**  
🏥 **Hospitals**  
🏬 **Malls & Enterprises**  
🏭 **Factories & Industries**  
🏛️ **Government & Military Institutions**  

---

## 🚀 **Key Features**  

- 🔹 **AI/ML-Powered Face Recognition** – Ultra-fast & accurate detection (99% precision).  
- 🔹 **Voice Assistant Integration 🎤** – Greets users, confirms attendance & guides fine payments.  
- 🔹 **Duplicate Prevention** – Each user can mark attendance **only once per lecture/shift**.  
- 🔹 **Real-Time Notifications** – Instant voice + visual feedback after attendance marking.  
- 🔹 **Fine Clearance System** – AI calculates fines for absentees with payment proof upload.  
- 🔹 **Voice-Controlled Search in History** – Query records by speaking **Name, Roll, or Subject**.  
- 🔹 **Cross-Platform** – Works on Web, Desktop, Raspberry Pi & Kiosk devices.  

---

## 🖼️ **How It Works (With Voice Assistant)**  

1️⃣ **Voice-Guided Face Registration** – Assistant guides students/employees during registration.  
2️⃣ **AI Recognition** – Face is scanned and matched in milliseconds.  
3️⃣ **Voice Feedback** – Assistant speaks:  
   - `"Hello Tony! Your attendance for OOMD has been marked ✅"`  
   - `"You have already marked attendance today ❌"`  
4️⃣ **Detailed Reporting** – Filter by **Subject, Date, Department** using **voice commands or text**.  
5️⃣ **Fine Clearance** – Voice-guided fine payment with QR & digital proof uploads.  

---

## 🔧 **Tech Stack**  

- **Frontend:** Streamlit  
- **Face Recognition:** dlib + face_recognition  
- **Voice Assistant:** pyttsx3 (TTS) + SpeechRecognition (STT)  
- **Data Management:** Pandas (CSV) or SQLite (upgradable to MySQL/Postgres)  
- **AI Models:** Deep CNN embeddings for facial features  

---

## 🎤 **Voice Assistant Demo Commands**  

- **Attendance:**  
  `"Hey NeuroFace, mark my attendance"`  
- **History Search:**  
  `"Show me OOMD attendance for Tony"`  
- **Fine Clearance:**  
  `"Do I have any pending fines?"`  

The assistant speaks back using **Text-to-Speech (TTS)** and can even be configured for **multiple languages 🌍**.

---

## 🛠️ Technology Stack

| Layer               | Technologies                               |
|---------------------|--------------------------------------------|
| **Frontend**        | Streamlit                                   |
| **Face Recognition**| dlib, face_recognition, Deep CNN Embeddings |
| **Voice Interface** | pyttsx3 (TTS), SpeechRecognition (STT)    |
| **Database**        | Pandas (CSV), SQLite (optionally MySQL/Postgres) |
| **AI Models**       | Deep Convolutional Neural Networks         |

## 🖥️ **Installation**  

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
