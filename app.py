import streamlit as st
import face_recognition
import numpy as np
import os
import datetime
import csv
import pandas as pd
from PIL import Image, UnidentifiedImageError

KNOWN_FOLDER = "known_faces"
ATTENDANCE_FILE = "attendance.csv"

st.set_page_config(page_title="Smart Classroom", layout="centered")

# Create required folders/files
os.makedirs(KNOWN_FOLDER, exist_ok=True)
if not os.path.exists(ATTENDANCE_FILE):
    with open(ATTENDANCE_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Roll", "Date", "Time","Status"])

# Sidebar selection
page = st.sidebar.radio("Choose Option", ["📸 Mark Attendance", "📝 Register Student", "📜 History","📕 Fine Clearance"])

# ===================== 📝 Register Student =====================
if page == "📝 Register Student":
    st.title("📝 Register New Student")

    name = st.text_input("Enter Student Name")
    roll = st.text_input("Enter Roll Number")

    st.markdown("### 📁 Upload Image or 📷 Take Photo")
    col1, col2 = st.columns(2)

    with col1:
        uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    with col2:
        webcam_photo = st.camera_input("Or Take a Photo")

    if name and roll:
        image_to_save = None

        if uploaded_file is not None:
            img = Image.open(uploaded_file).convert("RGB")
            image_to_save = np.array(img)
        elif webcam_photo is not None:
            img = Image.open(webcam_photo).convert("RGB")
            image_to_save = np.array(img)

        if image_to_save is not None:
            face_locations = face_recognition.face_locations(image_to_save)
            face_encodings = face_recognition.face_encodings(image_to_save, face_locations)

            if face_encodings:
                new_encoding = face_encodings[0]

                # Check for duplicate face
                known_encodings = []
                known_names = []

                for filename in os.listdir(KNOWN_FOLDER):
                    filepath = os.path.join(KNOWN_FOLDER, filename)
                    known_img = face_recognition.load_image_file(filepath)
                    known_encoding = face_recognition.face_encodings(known_img)
                    if known_encoding:
                        known_encodings.append(known_encoding[0])
                        known_names.append(filename)

                matches = face_recognition.compare_faces(known_encodings, new_encoding)

                if any(matches):
                    matched_index = matches.index(True)
                    existing_file = known_names[matched_index]
                    st.warning(f"⚠️ Face already registered as: {existing_file}")
                else:
                    # Save new face image
                    pil_img = Image.fromarray(image_to_save)
                    save_path = os.path.join(KNOWN_FOLDER, f"{name.lower()}_{roll}.jpg")
                    pil_img.save(save_path)
                    st.success(f"✅ {name} (Roll: {roll}) registered successfully.")
            else:
                st.error("❌ No face detected. Please upload or retake a clear photo.")
        else:
            st.info("📷 Please upload or take a photo.")
    else:
        st.info("✏️ Please fill in both Name and Roll.")

# ===================== 📸 Mark Attendance =====================
elif page == "📸 Mark Attendance":
    st.title("📸 Face Recognition Attendance System")

    @st.cache_data
    def load_known_faces():
        encodings, names, rolls = [], [], []
        for file in os.listdir(KNOWN_FOLDER):
            if file.endswith(('.jpg', '.png')):
                try:
                    img_path = os.path.join(KNOWN_FOLDER, file)
                    img = face_recognition.load_image_file(img_path)
                    encoding = face_recognition.face_encodings(img)
                    if encoding:
                        encodings.append(encoding[0])
                        name_part = file.split('.')[0]
                        if "_" in name_part:
                            name, roll = name_part.split("_", 1)
                        else:
                            name, roll = name_part, "Unknown"
                        names.append(name)
                        rolls.append(roll)
                except UnidentifiedImageError:
                    st.warning(f"⚠️ Skipping unreadable file: {file}")
        return encodings, names, rolls

    known_encodings, known_names, known_rolls = load_known_faces()

    lecture = st.selectbox("📚 Select Lecture", [
        "OOMD", "CF", "DB", "CIP", "DAA", "OS", "INS", "MAD", "CDT",
        "B1-OOMD", "B1-DB", "B1-OS", "B1-CF", "B1-INS",
        "B2-CF", "B2-OOMD", "B2-DB",
        "B3-CF", "B3-OOMD", "B3-DB", "B3-OS", "B3-INS",
        "Practice session", "Mentor"
    ])

    frame = st.camera_input("📸 Take a photo for attendance")

    if frame is not None:
        img = Image.open(frame).convert("RGB")
        img_np = np.array(img)

        face_locations = face_recognition.face_locations(img_np)
        face_encodings = face_recognition.face_encodings(img_np, face_locations)

        present_names = set()

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_names[best_match_index]
                roll = known_rolls[best_match_index]
                now = datetime.datetime.now()
                date = now.strftime('%Y-%m-%d')
                time = now.strftime('%H:%M:%S')

                with open(ATTENDANCE_FILE, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([name, roll, date, time, lecture])

                present_names.add(f"{name} ({roll})")

        if present_names:
            st.success(f"✅ Attendance Marked: {', '.join(present_names)} for {lecture}")
        else:
            st.error("❌ No recognized face found.")

    st.markdown("---")
    st.subheader("📄 Download Attendance")
    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, 'r') as f:
            st.download_button("⬇️ Download CSV", f.read(), file_name="attendance.csv")

# ===================== 📸 history =====================
elif page == "📜 History":
    st.title("📜 Attendance History")

    if os.path.exists(ATTENDANCE_FILE):
        # Load the CSV
        df = pd.read_csv(ATTENDANCE_FILE, names=["Name", "Roll", "Subject", "Date", "Time"], header=None)

        # Remove header row if duplicated
        if df.iloc[0]["Name"] == "Name":
            df = df[1:]

        # Drop missing or invalid entries
        df.dropna(subset=["Name", "Roll", "Subject", "Date", "Time"], inplace=True)
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
        df = df[df["Date"].notna()]

        # Normalize subject column (strip whitespace)
        df["Subject"] = df["Subject"].str.strip()

        # List of all known subjects
        all_subjects = sorted(set([
            "OOMD", "CF", "DB", "CIP", "DAA", "OS", "INS", "MAD", "CDT",
            "B1-OOMD", "B1-DB", "B1-OS", "B1-CF", "B1-INS",
            "B2-CF", "B2-OOMD", "B2-DB",
            "B3-CF", "B3-OOMD", "B3-DB", "B3-OS", "B3-INS",
            "Practice session", "Mentor"
        ] + df["Subject"].dropna().unique().tolist()))

        selected_subject = st.selectbox("📚 Filter by Subject", ["All"] + all_subjects)

        # Search input
        search_query = st.text_input("🔍 Search by Name or Roll:")

        # Apply filters
        filtered_df = df.copy()
        if selected_subject != "All":
            filtered_df = filtered_df[filtered_df["Subject"] == selected_subject]

        if search_query.strip():
            query = search_query.strip().lower()
            filtered_df = filtered_df[
                filtered_df["Name"].str.lower().str.contains(query, na=False) |
                filtered_df["Roll"].astype(str).str.contains(query, na=False)
            ]

        # Final results display
        if not filtered_df.empty:
            st.markdown("### 🧾 Filtered Attendance Records")
            st.dataframe(filtered_df)

            # 📊 Total Summary
            summary = filtered_df.groupby(["Name", "Roll"]).size().reset_index(name="Total Days Present")
            st.markdown("### 📊 Attendance Summary")
            st.dataframe(summary)

            # 📅 Weekly Summary
            filtered_df["Week"] = filtered_df["Date"].dt.strftime('%Y-W%U')
            weekly_summary = filtered_df.groupby(["Name", "Roll", "Week"]).size().reset_index(name="Days Present")
            st.markdown("### 📅 Weekly Attendance Summary")
            st.dataframe(weekly_summary)

            # 📚 Subject-wise Summary (only for 'All')
            if selected_subject == "All":
                subject_summary = filtered_df.groupby(["Name", "Roll", "Subject"]).size().reset_index(name="Subject-wise Attendance")
                st.markdown("### 📚 Subject-wise Summary")
                st.dataframe(subject_summary)

            # ⬇️ Download button
            st.download_button("⬇️ Download Filtered Data", filtered_df.to_csv(index=False), file_name="filtered_attendance.csv")

        else:
            st.warning("😕 No records match your filters.")
    else:
        st.info("📭 No attendance data found.")


# ===================== 📕 Fine Clearance =====================
elif page == "📕 Fine Clearance":
    st.title("📕 Fine Clearance System")

    # Check if absent file exists
    if os.path.exists("absent.csv"):
        df = pd.read_csv("absent.csv")

        # Show a search box for full student name
        name_query = st.text_input("🔍 Search by Full Name")

        if name_query:
            filtered_df = df[df["Name"].str.lower() == name_query.lower()]

            if filtered_df.empty:
                st.info("🙇 No absents found for this name.")
            else:
                selected_roll = filtered_df["Roll"].iloc[0]
                student_df = filtered_df[filtered_df["Status"] == "Absent"]

                if student_df.empty:
                    st.success("✅ No fines! You have no absent records.")
                else:
                    st.markdown(f"### 📅 Your Absent Lectures (Roll: {selected_roll})")
                    st.dataframe(student_df)

                    # Select which lectures to pay fine for
                    selected_rows = st.multiselect("Select lectures to clear fine for:", student_df.index)
                    fine_amount = len(selected_rows) * 10  # Rs.10 per lecture

                    if selected_rows:
                        st.markdown(f"### 💰 Total Fine: ₹{fine_amount}")

                        # QR Payment Section
                        st.markdown("#### 📲 Pay to the College UPI")
                        if os.path.exists("college_qr.png"):
                            st.image("college_qr.png", caption="Scan to Pay", width=300)
                        else:
                            st.warning("⚠️ QR code not found. Please ask admin.")

                        st.code("upi_id@bank", language="text")

                        # Upload Screenshot
                        st.markdown("#### 📤 Upload Payment Screenshot")
                        payment_proof = st.file_uploader("Upload Screenshot", type=["png", "jpg", "jpeg"])

                        if payment_proof:
                            uploads_dir = f"fine_uploads/{selected_roll}/"
                            os.makedirs(uploads_dir, exist_ok=True)
                            with open(os.path.join(uploads_dir, payment_proof.name), "wb") as f:
                                f.write(payment_proof.getbuffer())

                            st.success("✅ Payment proof uploaded. Your fine will be reviewed.")
                            st.markdown("🧾 Receipt will be generated after verification.")
        else:
            st.info("👆 Please enter your full name above to view fine details.")

    else:
        st.warning("⚠️ Absent record file 'absent.csv' not found.")
