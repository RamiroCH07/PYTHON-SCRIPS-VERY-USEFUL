import pandas as pd
import re
def Cont_Palabras(txt):
    txt = txt.strip()
    pals = txt.split()
    dic = dict()
    df = pd.DataFrame(columns = ['WORD','COUNT'])
    for pal in pals:
        pal = pal.lower()
        print(pal)
        pal = re.search(r'[a-zñáéíóú]+', pal)    
        pal = pal.group()
        print(pal)
        if dic.get(pal) == None:
            dic[pal] = 1
        else:
            dic[pal] = dic[pal] + 1
    
    for key in dic:
        value = dic[key]
        df.loc[df.shape[0]] = (key,value)
    return df
    