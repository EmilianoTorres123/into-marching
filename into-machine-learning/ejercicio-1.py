import pandas as pd


# Lee el archivo CSV en un DataFrame
home_data = pd.read_csv("train.csv", index_col=0)

# Muestra las primeras filas del DataFrame
print(home_data.head())


# Lee el archivo CSV en un DataFrame
melbourne_data = pd.read_csv("melb_data.csv", index_col=0)

# Muestra un resumen de los datos en el DataFrame
print(melbourne_data.describe())
