
import pandas as pd

from sklearn.tree import DecisionTreeRegressor


# Lee el archivo CSV en un DataFrame
home_data = pd.read_csv("train.csv", index_col=0)


y = home_data.SalePrice

# Check your answer
print(y)


# Create the list of features below
feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# Select data corresponding to features in feature_names
X = home_data[feature_names]

# Check your answer
print(X)


iowa_model = DecisionTreeRegressor(random_state=1)

# Entrena el modelo
iowa_model.fit(X, y)

# Imprime un mensaje de confirmación
print("El modelo de regresión de árbol de decisión se ha creado y entrenado exitosamente.")


# Predice el resultado del modelo en los mismos datos de entrenamiento
predictions = iowa_model.predict(X)

# Imprime las predicciones
print("Predicciones del modelo:")
print(predictions)

from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))


