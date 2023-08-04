import os
import shutil
data_folder = input('Enter folder name: ')

os.chdir(data_folder)

for filename in os.listdir('.'):
    if filename.endswith(('.jpg','.png','.jpeg','.webp')):
        os.makedirs('Images', exist_ok=True) # wenn da ist, nicht machen# makedir heißt mach folder
        shutil.move(filename,'Images') #python copy file to folder #python create a file if not exist

    elif filename.endswith(('.pdf','.doc','.docs','.csv','.pptx','.epub','.odt')):
        os.makedirs('Docs', exist_ok=True)
        shutil.move(filename,'Docs')

    elif filename.endswith(('.mp4','.mp3','.avi')):
        os.makedirs('Media', exist_ok=True)
        shutil.move(filename,'Media')

    elif filename.endswith(('.tar','.rar','.zip')):
        os.makedirs('Archiv', exist_ok=True)
        shutil.move(filename,'Archiv')

    elif filename.endswith(('.py','.js','.css','.html')):
        os.makedirs('Code', exist_ok=True)
        shutil.move(filename,'Code')



print('DONE......')