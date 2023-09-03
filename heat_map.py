import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Edirne': [31.2, 33.3,32.4, 33.1, 34],
    'Tekirdağ': [35, 34, 33, 32, 31],
    'Kırkalreli': [32, 33, 34, 35.5, 36],
    'İstanbul': [36, 34, 33.8, 32.4, 31.5],
    'Çanakkale': [35, 34, 33, 32, 31],
    'Ankara': [36,36.2,36.4,36.8,32],
    'Bolu':[29,28,27,26,30],
    'Bursa':[27,28,30,25,32],
    'Muğla':[23,22,31,45,11]
}
df = pd.DataFrame(data)

# Kolerasayon
correlation_matrix = df.corr()

# Seaborn ile görselleştir
plt.figure(figsize=(8, 6))
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

