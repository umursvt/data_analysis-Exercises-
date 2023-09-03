import pandas as pd

data = { 
    'A':[1,2,None,4],
    'B':[5,6,3,2]
}

df=pd.DataFrame(data)

df_cleaned = df.dropna() # Eksik değerleri çıkar
df_filled = df.fillna('YOK')  # Eksik değerlerin yerine yok yaz

print(df_filled)
print(df_cleaned)


