import qrcode
import pandas as pd
import os

# Student data
students = [
    {"Name": "Aditya", "Dept": "AIML"},
    {"Name": "Nikita", "Dept": "AIML"},
    {"Name": "Pratiksha", "Dept": "AIML"},
    {"Name": "Nikhil", "Dept": "AIML"},
    {"Name": "Prathmesh", "Dept": "AIML"}
]

# Create folder for QR images
qr_folder = "qr_images"
os.makedirs(qr_folder, exist_ok=True)

# List for CSV data
data_for_csv = []

for student in students:
    
    # Format info for QR code
    info = f"{student['Name']}|{student['Dept']}"
    
    # Generate QR Code
    qr = qrcode.make(info)
    
    # QR filename (use name)
    qr_filename = f"{student['Name']}.png"
    qr_path = os.path.join(qr_folder, qr_filename)
    
    # Save QR image
    qr.save(qr_path)
    
    # Save data for CSV
    data_for_csv.append({
        "Name": student['Name'],
        "Dept": student['Dept'],
        "QRCode_Path": qr_path
    })

# Convert to DataFrame
df = pd.DataFrame(data_for_csv)

# Save CSV
df.to_csv("students_with_qr.csv", index=False)

print("All QR codes generated and CSV created successfully.")