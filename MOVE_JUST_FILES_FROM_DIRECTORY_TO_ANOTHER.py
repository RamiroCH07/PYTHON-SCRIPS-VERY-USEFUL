import os
import shutil
counter = 0
#print("If you want all the excel file, for example write .xlsx")
##inp = input("What are you looking for?:> ")

def COPY_JUST_FILES_FROM_DIRECTORY_TO_ANOTHER(source_dir,destination_dir,format_files):
    count = 0
    for root,subdirs,files in os.walk(source_dir):
        for file in files:
            for format in format_files:
                if format in file:
                    count+=1
                    full_path_file = os.path.join(root, file)
                    print("COPIANDO ARCHIVO "+ format)
                    shutil.copy(full_path_file, destination_dir)
                    break
    print('SE COPIARON '+str(count)+' ARCHIVOS')

source_dir = 'G:\BK_CASA_CUSCO_07_08_23\RECUPERADO_H\FOTOS'
destination_dir = 'G:\BK_CASA_CUSCO_07_08_23\RECUPERADO_H\FOTOS_RECOPILADOS'
format_files = ['.jpg','.png','.mp4']

COPY_JUST_FILES_FROM_DIRECTORY_TO_ANOTHER(source_dir,destination_dir,format_files)
