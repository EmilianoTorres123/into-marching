import pandas as pd
home_data = pd.read_csv("train.csv", index_col=0)

# Import the train_test_split function and uncomment
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
# fill in and uncomment
# Define la lista de características
feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# Selecciona los datos correspondientes a las características en feature_names y almacénalos en X
X = home_data[feature_names]

# Columna objetivo
y = home_data.SalePrice

# Divide los datos en conjuntos de entrenamiento y validación
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Imprime las dimensiones de los conjuntos resultantes
print("Dimensiones del conjunto de entrenamiento (train_X, train_y):", train_X.shape, train_y.shape)
print("Dimensiones del conjunto de validación (val_X, val_y):", val_X.shape, val_y.shape)

# Define la lista de características
feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# Selecciona los datos correspondientes a las características en feature_names y almacénalos en X
X = home_data[feature_names]

# Columna objetivo
y = home_data.SalePrice

# Divide los datos en conjuntos de entrenamiento y validación
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Define el modelo de regresión de árbol de decisión con random_state
iowa_model = DecisionTreeRegressor(random_state=1)

# Ajusta el modelo con los datos de entrenamiento
iowa_model.fit(train_X, train_y)

# Imprime un mensaje de confirmación
print("El modelo de regresión de árbol de decisión se ha ajustado exitosamente con los datos de entrenamiento.")

# Define la lista de características
feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# Selecciona los datos correspondientes a las características en feature_names y almacénalos en X
X = home_data[feature_names]

# Columna objetivo
y = home_data.SalePrice

# Divide los datos en conjuntos de entrenamiento y validación
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Define el modelo de regresión de árbol de decisión con random_state
iowa_model = DecisionTreeRegressor(random_state=1)

# Ajusta el modelo con los datos de entrenamiento
iowa_model.fit(train_X, train_y)

# Realiza predicciones en los datos de validación
val_predictions = iowa_model.predict(val_X)

# Imprime las predicciones en los datos de validación
print("Predicciones en los datos de validación:")
print(val_predictions)

val_mae = mean_absolute_error(val_y, val_predictions)

# Suponiendo que tienes tus datos de validación en las variables val_y y val_predictions
val_mae = mean_absolute_error(val_y, val_predictions)

# Imprimir el valor del MAE
print(val_mae)



#ejemplos-del tema
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error


# Define la lista de características
feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# Selecciona los datos correspondientes a las características en feature_names y almacénalos en X
X = home_data[feature_names]

# Columna objetivo
y = home_data.SalePrice

# Define el modelo de regresión de árbol de decisión con random_state
melbourne_model = DecisionTreeRegressor(random_state=1)

# Ajusta el modelo
melbourne_model.fit(X, y)

# Realiza predicciones
predicted_home_prices = melbourne_model.predict(X)

# Calcula el error absoluto medio
mae = mean_absolute_error(y, predicted_home_prices)

# Imprime el valor del error absoluto medio (MAE)
print("Mean Absolute Error (MAE):", mae)

from sklearn.metrics import mean_absolute_error

# Suponiendo que tienes tus datos de validación en las variables val_y y val_predictions
val_mae = mean_absolute_error(val_y, val_predictions)

# Imprimir el valor del MAE
print(val_mae)



from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pandas as pd

# Lee el archivo CSV en un DataFrame
home_data = pd.read_csv("train.csv", index_col=0)

# Define la lista de características
feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# Selecciona los datos correspondientes a las características en feature_names y almacénalos en X
X = home_data[feature_names]

# Columna objetivo
y = home_data.SalePrice

# Divide los datos en conjuntos de entrenamiento y validación
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

# Define el modelo de regresión de árbol de decisión
melbourne_model = DecisionTreeRegressor()

# Ajusta el modelo con los datos de entrenamiento
melbourne_model.fit(train_X, train_y)

# Realiza predicciones en los datos de validación
val_predictions = melbourne_model.predict(val_X)

# Calcula el error absoluto medio en los datos de validación
mae = mean_absolute_error(val_y, val_predictions)

# Imprime el valor del error absoluto medio (MAE) en los datos de validación
print("Mean Absolute Error (MAE) on Validation Data:", mae)
