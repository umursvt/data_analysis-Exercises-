import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 28]}

df = pd.DataFrame(data)

filtered_df = df[df['Age']>25]
print(filtered_df)