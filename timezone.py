import pandas as pd

df = pd.read_csv('timezone.csv')

print(df.head())



df = df['cities'].apply(lambda x:x.split("/"))
print(df)

df[['Country', 'City']] = pd.DataFrame(df['cities'].tolist(), index=df.index)
print(df)