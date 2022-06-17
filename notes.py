import pandas as pd

df = pd.read_csv('pokemon_data.csv', delimiter=',')
# print(df)

# print(df.columns)                               # reads columns

# print(df['Name'])                               # only get the name of the pokemons

# print(df['Name'][0:5])                          # use slicing to only get first 5 

# to get multiple items at the same time, instead of only getting the column name you can insert a list instead print(df[['Name', 'Type 1', 'HP']])

"""
ILOC - used for index """

# to get just a row
# print(df.head(4))
# print(df.iloc[1])
# print(df.iloc[1:4])

# iloc to get a specific location, i.e) just getting the Venusaur
# pass in the second row first column
# print(df.iloc[2,1])

"""iterating through rows"""

for index, row in df.iterrows():
    # print(index, row)
    # print(index, row['Name'])
    pass


"""LOC - used for textual """

print(df.loc[df['Type 1'] == 'Fire' ]) # only get fires
print(df.loc[df['Type 1'] == 'Grass'])