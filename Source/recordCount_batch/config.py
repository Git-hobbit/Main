from datetime import datetime
import os
import csv

today = datetime.today().strftime('%Y-%m-%d')
timestamp = datetime.today().strftime('%y%m%d_%H%M%S')
output_filename = f'MP_BATCH_TRIGGER_{timestamp}.csv'
prefix = 'MP_BATCH_TRIGGER'
root_path = 'C:/Users/IXR1204/OneDrive - Stanley Black & Decker/Documents/CHR_CSV'
folder_path = os.path.join(root_path,today)                                # This is the path to the folder with the current date
#print(folder_path)
output_path = os.path.join(folder_path,output_filename)                    # This is the path to the BATCH file
temp_RP = os.path.join(root_path,output_filename)
#print(temp_RP)
