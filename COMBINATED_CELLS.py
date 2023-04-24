#TRATAMIENTO DE CELDAS COMBINADAS USANDO OPENPYXL

import openpyxl as xl
import pandas as pd

#Cargamos el archivo de excel
libro = xl.load_workbook('PRUEBA.xlsx',data_only=True)
#Accedemos a una hoja
hoja = libro['Hoja1']

#Inicializamos un objeto DF
df = pd.DataFrame(columns = [i for i in range(1,7)])   
# posicionamiento en fila desde donde inician los datos a extraer
start = 2
# posicionamiento en fila donde terminan los datos a extraer
finish = 9

# Recorremos las filas de interes
for i in range(start,finish):
    # Obtenermos la fila
    row = hoja[f'A{i}':f'F{i}'][0]
    lrow = []
    # Inicializamos la fila para df
    fil = i-start
    # Iteramos cada elemento de la fila
    for col,element in enumerate(row):
        # Si el elemento es parte de una celda combinada entonces copia el valor de arriba del df
        if type(element).__name__ == 'MergedCell':
            lrow.append(df.iloc[fil-1,col])
        # Si el elemento no es parte de una celda combinada agrega el valor del elemento    
        else:
            lrow.append(element.value)
    df.loc[df.shape[0]] = lrow
            

        