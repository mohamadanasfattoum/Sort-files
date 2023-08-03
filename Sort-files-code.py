import os
import shutil
data_folder = input('Enter folder name: '),

os.chdir(data_folder)

for filename in os.listdir('.'):
    if filename.endswith(('.jpg','.png','.jpeg')):
        os.makedirs('Images', exist_ok=True) # wenn da ist, nicht machen# makedir heißt mach folder
        shutil.move(filename,'Images') #python copy file to folder #python create a file if not exist