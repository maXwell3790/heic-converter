from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from pillow_heif import register_heif_opener
import os

counter = 0

register_heif_opener()

start_dir = filedialog.askdirectory(mustexist=True)
print('Suche wird gestartet..')
files = [datei for datei in os.listdir(start_dir) if datei.endswith('.heic')]
for file in files:
    file_path = os.path.join(start_dir, file)
    temp_img = Image.open(file_path)
    jpg_img = file_path.replace('.HEIC', '.jpg')
    temp_img.save(jpg_img)
    counter += 1
messagebox.showinfo('Erledigt', f'{counter} Bilder wurden konvertiert.')
