import json
import os
import gspread
import pandas as pd
from google.oauth2.credentials import Credentials


GOOGLE_API_CREDENTIALS = json.loads(os.getenv("GOOGLE_API_CREDENTIALS"))


def update_spreadsheet_from_google(
    spreadsheet_id: str = '',
    worksheet_name: str = '',
    excel_filename: str = '',
    token: dict = {},
    file_path: str = '',
):
    """Pull and update a spreadsheet from a Google Sheet to an excel file."""
    creds = Credentials.from_authorized_user_info(token)
    gc = gspread.authorize(creds)

    sh = gc.open_by_key(spreadsheet_id)
    worksheet = sh.worksheet(worksheet_name)
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    print(df.head())
    print("Writing to:", os.path.join(file_path, excel_filename))
    df.to_excel(os.path.join(file_path, excel_filename), index=False)


update_spreadsheet_from_google(
    spreadsheet_id='1pO2RJgHw2WDQkZWopqkqRXo5LRe_EtWFkJQCuHZ8pCM',
    worksheet_name='DBs',
    excel_filename="Cloud_DBs.xlsx",
    token=GOOGLE_API_CREDENTIALS,
    file_path='excel',
)
