import pandas as pd

data = {'Nombre': ['Juan', 'Ana', 'Pedro'],
        'Edad': [25, 30, 22],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']}

df = pd.DataFrame(data)
print(df)