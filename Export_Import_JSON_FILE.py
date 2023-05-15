import json 
lista_dic = [
    {'COMPRA': 3.311, 'VENTA': 3.317, 'FECHA': '2020-01-01'},
    {'COMPRA': 3.308, 'VENTA': 3.311, 'FECHA': '2020-01-03'},
    {'COMPRA': 3.318, 'VENTA': 3.32, 'FECHA': '2020-01-08'},
    {'COMPRA': 3.321, 'VENTA': 3.324, 'FECHA': '2020-01-11'}
  ]

## Importar una lista de diccionarios como json file
with open("prueba_json.json","w") as f:
    json.dump(lista_dic,f)
#%% Exportando una lista de diccionarios(archivo json)
with open("prueba_json.json","r") as f:
    json_object = json.load(f)

