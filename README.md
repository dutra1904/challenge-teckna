# Google Sheets Grade Calculator

This application calculates student grades and attendance based on data from a Google Sheet. It applies predefined rules to determine if a student is approved, needs a final test, or has failed.

---

## Technologies Used  
- **Python**  
- **Google Sheets API**  
- **Pandas**

## Features  
✅ Read data from a Google Sheets spreadsheet  
✅ Calculate the average of grades P1, P2 and P3  
✅ Check students' status (Pass, Fail, Final Exam.)  
✅ Calculate the minimum passing grade if necessary  
✅ Update spreadsheet results

---

## How to perform
### 1️⃣ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/dutra1904/challenge-teckna.git

2. Navigate to the project folder:
   ```bash
   cd project-folder

  3. Intall the dependencies:
     ```bash
     pip install -r requirements.txt

### 2️⃣ Setting up Google Sheets API Credentials

To run this project, you need to create a service account and download the credentials file.

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Enable the "Google Sheets API" and "Google Drive API" for the project.
4. Create a service account and generate a JSON key file.
5. Download the JSON key file and rename it to `challenge-maria-clara.json`.
6. Place the file in the root directory of this project.

### 3️⃣ Spreadsheet Link
You can view the Google Sheet used by the application here: [Click here or the image to access the spreadsheet](https://docs.google.com/spreadsheets/d/1B8LbphaK66cEvUmg0NK69WXAf7JzmkdcN46PF-cA6No/edit?usp=sharing)

[![Picture of the Spreadsheet](https://github.com/user-attachments/assets/62729fb3-386a-4deb-924e-5c8c353075c6)](https://docs.google.com/spreadsheets/d/1B8LbphaK66cEvUmg0NK69WXAf7JzmkdcN46PF-cA6No/edit?usp=sharing)
   > You can change any of these headears `P1`, `P2`, `P3`, `Faltas`. And see how the program operate

### 4️⃣ Putting Google Sheets API Credentials in Googlesheets File

1. After create the JSON key, Open the JSON file and find the `"client_email"` field. It will look something like this:"client_email": "your-service-account@your-project-id.iam.gserviceaccount.com".
2. Open the Google Sheets file that will be used in the project: [Click here to acess the Google Sheets File](https://docs.google.com/spreadsheets/d/1B8LbphaK66cEvUmg0NK69WXAf7JzmkdcN46PF-cA6No/edit?usp=sharing).
3. Share the sheet with the `client_email` you found in step 1, granting **Editor** permissions.![image](https://github.com/user-attachments/assets/bb172f68-dc08-4898-9d8c-953795f06f59)
   > Paste the  `client_email` Here



### 5️⃣ Running the Application

  After doing all these steps ,Run the script using Python:
  ```bash
  python main.py
````
---

## ⚙️ Logging 

The application includes logging to monitor activities such as:

- Authentication with the Google Sheets API.
- Reading data from the spreadsheet.
- Calculating grades and attendance.
- Updating the spreadsheet with results.
  
Logs will be printed to the console for easy debugging.

## ⚙️ Notes 

- Ensure that the file `challenge-maria-clara.json` with the service account credentials is placed in the project root directory.
- Replace `SPREADSHEET_ID` in the spreadsheet link above with the actual ID of your Google Sheet.
- Make sure the spreadsheet headers match the expected format: `P1`, `P2`, `P3`, `Faltaas`, `Situação`, and `Nota para Aprovação Final`.

   > Made by Maria Clara Dutra
