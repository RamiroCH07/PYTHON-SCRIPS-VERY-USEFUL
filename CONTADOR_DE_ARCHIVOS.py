import os 
#dir_path = r'C:\Users\rchavez\PROYECTOS\-prod-etl_project_potencias_contratadas'
dir_path = os.getcwd()
count = 0

for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        print(os.path.join(dir_path, path))
        count += 1
print('File count:', count)
