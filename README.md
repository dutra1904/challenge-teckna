# Google Sheets Grade Calculator

This application calculates student grades and attendance based on data from a Google Sheet. It applies predefined rules to determine if a student is approved, needs a final test, or has failed.

## Installation

1. Clone this repository:
   ```bash
   git clone <https://github.com/dutra1904/challenge-teckna.git>

2. Navigate to the project folder:
   ```bash
   cd project-folder

  3. Intall the dependencies:
     ```bash
     pip install -r requirements.txt

  ## Running the Application
  Run the script using Python:
  ```bash
  python main.py
````

## Spreadsheet Link
You can view the Google Sheet used by the application here: [Click here to access the spreadsheet](https://docs.google.com/spreadsheets/d/1B8LbphaK66cEvUmg0NK69WXAf7JzmkdcN46PF-cA6No/edit?usp=sharing)

## Logging 

The application includes logging to monitor activities such as:

- Authentication with the Google Sheets API.
- Reading data from the spreadsheet.
- Calculating grades and attendance.
- Updating the spreadsheet with results.
  
Logs will be printed to the console for easy debugging.

## Notes 

- Ensure that the file `challenge-maria-clara.json` with the service account credentials is placed in the project root directory.
- Replace `SPREADSHEET_ID` in the spreadsheet link above with the actual ID of your Google Sheet.
- Make sure the spreadsheet headers match the expected format: `P1`, `P2`, `P3`, `Absences`, `Status`, and `FinalGradeRequirement`.





