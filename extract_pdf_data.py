import pdfplumber
import os
import pandas as pd

# Step 1: Set the folder paths
pdf_folder = r"C:\Users\user\Downloads\PDF_Extraction"  # Change this to the folder where your PDFs are stored
output_excel = "extracted_data.xlsx"

# Step 2: Create an empty list to store the data
data = []

# Step 3: Loop through each PDF in the folder
for file_name in os.listdir(pdf_folder):
    if file_name.endswith(".pdf"):
        file_path = os.path.join(pdf_folder, file_name)
        try:
            with pdfplumber.open(file_path) as pdf:
                patient_name = "brack"
                emergency_name = "brack"
                emergency_phone = "brack"  # Default value if no name is found
                for page in pdf.pages:
                    text = page.extract_text()
                    if "Name:" in text:  # Adjust this if the format differs
                        patient_name = text.split("Name:")[1].split("\n")[0].strip()
                    if "Emergency Contact:" in text:  # Adjust this if the format differs
                        emergency_name = text.split("Emergency Contact:")[1].split("\n")[0].strip()
                    if "Emergency Contact Phone:" in text:  # Adjust this if the format differs
                        emergency_phone = text.split("Emergency Contact Phone:")[1].split("\n")[0].strip()
                        break
                # Append the data (file name and patient name) to the list
                data.append({"File Name": file_name, "Patient Name": patient_name, "Emergency Contact": emergency_name, "Emergency Phone": emergency_phone})
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

# Step 4: Convert the data into an Excel file
df = pd.DataFrame(data)
df.to_excel(output_excel, index=False)
print(f"Data saved to {output_excel}")
