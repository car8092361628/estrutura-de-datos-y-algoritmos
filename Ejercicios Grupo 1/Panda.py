import pandas as pd

data={
    'Nombre': ['Juan', 'Ana', 'Pedro', 'Maria'],
    'Edad': [28, 22, 35, 30],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla'],
}

tabla=pd.DataFrame(data)
print(tabla)