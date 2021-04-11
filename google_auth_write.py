#!/usr/bin/env python
# coding: utf-8

# In[18]:


from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from pprint import pprint


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1HRpjR7VKiyH5NrL4f50IM1im6WrFGbs5g-i7tu1fJk0'
RANGE_NAME = 'levels!A1:E400'

def write_playbook(values):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    
    body = {
        'values': values
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, valueInputOption='USER_ENTERED', body=body).execute()
    pprint(result)
    
if __name__ == '__main__':
    value = [['level', 'id', 'description', 'type', 'target'], ['003', '0', '실시간 미터 이미지 취득 시스템 구축', 'mission', ''], ['003', '1', '이미지로부터 인식대상 숫자부분을 추출', 'mission', ''], ['003', '2', '숫자 추출 프로그램', 'mission', ''], ['003', '3', 'get number via calling google tesseract with image', 'mission', ''], ['003', '5', 'make labelling and build training dataset from files', 'mission', ''], ['003', '6', 'apply your dataset to MNIST', 'mission', ''], ['001', '1', 'Date Store', 'mission', 'student'], ['001', '2', 'Data Explore & Preprocess', 'mission', 'student'], ['001', '3', 'Data Analysis', 'mission', 'student'], ['001', '4', 'Modeling', 'mission', 'student'], ['002', '1', 'data store', 'mission', 'student'], ['002', '2', 'data analysis', 'mission', 'student'], ['002', '3', 'data split', 'mission', 'student'], ['002', '4', 'image_data_generator', 'mission', 'student'], ['002', '5', 'CNN modeling', 'mission', 'student'], ['002', '6', 'estimation', 'mission', 'student']]
    write_playbook(value)


# In[ ]:




