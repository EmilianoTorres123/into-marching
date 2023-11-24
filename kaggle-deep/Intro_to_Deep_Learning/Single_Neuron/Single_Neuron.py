import pandas as pd

red_wine = pd.read_csv('../CSV/red-wine.csv')
red_wine.head()

rows, columns = red_wine.shape
print(f'The dataframe has {rows} rows and {columns} columns.')
#red_wine.shape (1, 12)# (rows, columns)
# YOUR CODE HERE
input_shape = [11]

print(input_shape)