import pandas as pd
data = {'Department': ['HR', 'IT', 'HR', 'Finance', 'IT'],
        'Salary': [5000, 6000, 5500, 7000, 6500]}

df = pd.DataFrame(data)

# Departmanlara göre maaşların ortalamasını hesaplama
df_mean = df.groupby('Department')['Salary'].mean()

# Departmanlara göre en yüksek maaşı veirr
df_max = df.groupby('Department')['Salary'].max()

# Departmanlara göre en az maaşı veirr
df_min = df.groupby('Department')['Salary'].min()

# Departmana göre toplam maaş miktarını verir
df_sum =df.groupby('Department')['Salary'].sum()
print(df_sum)
