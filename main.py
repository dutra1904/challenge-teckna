import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import math
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Authenticating with Google Sheets API.")

# Authentication with Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("challenge-maria-clara.json", scope)
client = gspread.authorize(creds)
logging.info("Fetching data from the spreadsheet.")

# Opening the spreadsheet
spreadsheet = client.open_by_key("1B8LbphaK66cEvUmg0NK69WXAf7JzmkdcN46PF-cA6No")
sheet = spreadsheet.sheet1  # Seleciona a primeira aba

# Fetching all rows from the spreadsheet
all_values = sheet.get_all_values()

# Getting the correct headers
headers = all_values[2]  # Line 3 of the spreadsheet contains the correct headers
rows = all_values[3:]  # Data starts at line 4

# Transforming data into dictionaries
data = [dict(zip(headers, row)) for row in rows]
logging.info("Processing data and calculating results.")

# Converting to Pandas DataFrame
df = pd.DataFrame(data)

# Converting columns to numeric
df["P1"] = pd.to_numeric(df["P1"])
df["P2"] = pd.to_numeric(df["P2"])
df["P3"] = pd.to_numeric(df["P3"])
df["Faltas"] = pd.to_numeric(df["Faltas"])

# Business Rules
TOTAL_CLASSES = 60    
APPROVAL_THRESHOLD = 7.0
FINAL_TEST_THRESHOLD = 5.0
ABSENCE_LIMIT = 0.25 * TOTAL_CLASSES

def calculate_status(row):
    avg = (row["P1"] + row["P2"] + row["P3"]) / 3
    absences = row["Faltas"]
    
    if absences > ABSENCE_LIMIT:
        return "AbsentFailed for Absence", 0
    elif avg >= APPROVAL_THRESHOLD:
        return "Approved", 0
    elif avg >= FINAL_TEST_THRESHOLD:
        fga = math.ceil(10 - avg)        
        return "Final Test", fga
    else:
        return "Failed by Grade", 0
    

# Applying rules to each student
logging.info("Updating the spreadsheet with new results.")
df["Situação"], df["Nota para Aprovação Final"] = zip(*df.apply(calculate_status, axis=1))

# Updating only the "Status" and "FinalGradeRequirement" columns in the spreadsheet
situation_column_index = headers.index("Situação") + 1  
final_grade_column_index = headers.index("Nota para Aprovação Final") + 1

situation_values = df["Situação"].tolist()
final_grade_values = df["Nota para Aprovação Final"].tolist()

# Batch update to avoid exceeding quota
for i, (situation, final_grade) in enumerate(zip(situation_values, final_grade_values), start=4):  # Começa na linha 4
    sheet.update_cell(i, situation_column_index, situation)
    sheet.update_cell(i, final_grade_column_index, final_grade)

print("Spreadsheets updated!")