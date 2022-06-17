import pandas as pd

df = pd.read_csv('pokemon_data.csv', delimiter=',')
# print(df)

# print(df.columns)                               # reads columns

# print(df['Name'])                               # only get the name of the pokemons

print(df['Name'][0:5])                            # use slicing to only get first 5