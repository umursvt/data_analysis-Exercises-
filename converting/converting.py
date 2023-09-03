import pandas as pd 

data = {'Date':['2023-08-01','2023-08-02','2023-08-03'],
        'Temperature': [24,22,26]
        }

df = pd.DataFrame(data)

# Tarih sutununu datetime tipine çevir
df['Date'] = pd.to_datetime(df['Date'])

df['Celsius'] = (df['Temperature']-32)*5/9

print(df)