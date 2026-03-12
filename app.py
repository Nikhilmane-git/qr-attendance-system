import streamlit as st
import cv2
import pandas as pd
from datetime import datetime

st.title("📷 QR Code Attendance System")

# Load dataset
df = pd.read_csv("students_with_qr.csv")
marked_attendance = set()

run = st.checkbox("Start Camera")

FRAME_WINDOW = st.image([])

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while run:
    ret, frame = cap.read()
    if not ret:
        st.write("Camera not working")
        break

    data, bbox, _ = detector.detectAndDecode(frame)

    if data:
        # Now only Name and Dept
        name, dept = data.split('|')

        if name not in marked_attendance:
            marked_attendance.add(name)

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open("attendance_log.csv", "a") as f:
                f.write(f"{name},{dept},{now}\n")

            st.success(f"Attendance Marked: {name}")

        if bbox is not None:
            pts = bbox.astype(int).reshape(-1, 2)

            for i in range(len(pts)):
                pt1 = tuple(pts[i])
                pt2 = tuple(pts[(i + 1) % len(pts)])
                cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

            cv2.putText(frame, f"{name} | {dept}",
                        (pts[0][0], pts[0][1]-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (255,0,0),
                        2)

    FRAME_WINDOW.image(frame, channels="BGR")

cap.release()