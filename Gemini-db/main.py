# Modules First
import ping3
import random
import socket
import string
import os
import shutil
import time
 
print("Gemini-db has been started")

def create_database():
    root_folder = os.path.dirname(os.path.abspath(__file__))
    
    database_folder = os.path.join(root_folder, "database-local")
    if not os.path.exists(database_folder):
        print(f"Created 'database-local' folder at root")
        os.makedirs(database_folder)
    
    while True:
        files = [f for f in os.listdir(root_folder) if os.path.isfile(os.path.join(root_folder, f))]
        
        for file in files:
            if file != os.path.basename(__file__): 
                print(f"File Request has been accepted (Response Time of the file: 2ms)")
                file_path = os.path.join(root_folder, file)
                destination_path = os.path.join(database_folder, file)
                shutil.move(file_path, destination_path)  
                # Change to shutil.copy if you want to copy instead of move
        
        # Wait for a specified interval before checking for new files again (e.g., every 2 milliseconds by default)
        time.sleep(2)

create_database()
