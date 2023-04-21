import glob
import os.path
import shutil

#%% Identifacamos el ultimo archivo descargado con formato xlsx
folder_path = r'C:\Users\Toshiba\Downloads'
file_type = r'\*xlsx'
files = glob.glob(folder_path + file_type)
max_file = max(files, key=os.path.getctime)
#%% Movemos el archivo descargado a una carpeta dentro del proyecto
source = fr'{max_file}'
## Nuevo nombre de archivo
destination = "./FUNCIONO.xlsx"
shutil.move(source,destination)
