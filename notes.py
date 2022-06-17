import pandas as pd

df = pd.read_csv('pokemon_data.csv', delimiter=',')
df.columns
df['Name']
df['Name'][0:5]
df[['Name', 'Type 1', 'HP']]

"""print(df)
print(df.columns)                               # reads columns
print(df['Name'])                               # only get the name of the pokemons
print(df['Name'][0:5])                          # use slicing to only get first 5 
 to get multiple items at the same time, instead of only getting the column name you can insert a list instead 
print(df[['Name', 'Type 1', 'HP']])
"""
"""

ILOC - used for index """
"""to get just a row
print(df.head(4))
print(df.iloc[1])
print(df.iloc[1:4]) using iloc
iloc to get a specific location, i.e) just getting the Venusaur
pass in the second row first column
print(df.iloc[2,1])"""
df.head(4)
df.iloc[1]
df.iloc[1:4]
df.iloc[2,1]

"""iterating through rows"""

for index, row in df.iterrows():
    # print(index, row)
    # print(index, row['Name'])
    pass


"""LOC - used for textual """

# print(df.loc[df['Type 1'] == 'Fire' ]) # only get fires
# print(df.loc[df['Type 1'] == 'Grass'])

"""
Using df.describe() method to get high level standard deviation stats
print(df.describe())
print(df.sort_values('Name', ascending=False))
print(df.sort_values(['Type 1', 'HP'])
print(df.sort_values(['Type 1', 'HP'], ascending=False))"""
df.describe()
df.sort_values('Name', ascending=False)

df.sort_values(['Type 1', 'HP'], ascending=[1,0])            # to select oder for both

"""Making changes to data
adding column 
HP  ...  Sp. Atk  Sp. Def  Speed  --> adding all those up to get the total and we are creating the total column
columns = vertical rows = horizontal"""

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + ['Speed']

print(df)

"""
NOTE
when printing: ufunc 'add' did not contain a loop with signature matching types (dtype('int64'), dtype('<U5')) -> None

you gotta change the data types to match the same ones in order to be able to add them like we are trying to do right here"""
