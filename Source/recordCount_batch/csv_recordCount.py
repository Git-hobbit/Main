from datetime import datetime
from config import *
import os
import csv

def generate_file():
    loadFileNames = []
    loadFileNames.clear()
   
    for file in os.listdir(root_path):
        if file.lower().endswith('.csv'):
            file_path = os.path.join(root_path,file)
            with open(file_path,'r',newline='',encoding = 'utf-8') as f:
                reader = csv.reader(f)
                header = next(reader,None)
                record_count = sum(
                    1 for row in reader
                    if row and row[0].strip()
                )
                loadFileNames.append([file,record_count])
   
    with open(temp_RP,'w',newline='',encoding='utf-8') as f:
        writer = csv.writer(f,delimiter=',')
        writer.writerows(loadFileNames)
   
    print("File successfully generated!")
   
                           

for file in os.listdir(root_path):
    present = False
    if file.startswith(prefix):
        present = True
        break
   

if present:
    user_input = input("Batch file is already present. Do you want to create a new file with current timestamp? Y/N :  ").strip().lower()
    if user_input =='y':
        generate_file()
else:
    generate_file()      


