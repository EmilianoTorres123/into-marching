
# Código para cargar los datos con la ruta de entrada especificada
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Configurar la verificación de código
import os
if not os.path.exists("train.csv"):
    os.symlink("input/home-data-for-ml-course/train.csv", "train.csv")  
    os.symlink("input/home-data-for-ml-course/test.csv", "test.csv") 
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex7 import *

# Cargar los datos utilizando la ruta de entrada especificada
home_data = pd.read_csv("train.csv", index_col=0)

# Crear el objetivo y llamarlo 'y'
y = home_data.SalePrice
# Crear 'X'
caracteristicas = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[caracteristicas]

# Dividir los datos en conjunto de validación y entrenamiento
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Especificar el modelo
modelo_iowa = DecisionTreeRegressor(random_state=1)
# Ajustar el modelo
modelo_iowa.fit(train_X, train_y)

# Hacer predicciones en el conjunto de validación y calcular el error absoluto medio
predicciones_val = modelo_iowa.predict(val_X)
mae_val = mean_absolute_error(predicciones_val, val_y)
print("MAE de validación sin especificar max_leaf_nodes: {:,.0f}".format(mae_val))

# Usar el mejor valor para max_leaf_nodes
modelo_iowa = DecisionTreeRegressor(max_leaf_nodes=100, random_state=1)
modelo_iowa.fit(train_X, train_y)
predicciones_val = modelo_iowa.predict(val_X)
mae_val = mean_absolute_error(predicciones_val, val_y)
print("MAE de validación para el mejor valor de max_leaf_nodes: {:,.0f}".format(mae_val))

# Definir el modelo. Establecer random_state en 1
modelo_rf = RandomForestRegressor(random_state=1)
modelo_rf.fit(train_X, train_y)
predicciones_val_rf = modelo_rf.predict(val_X)
mae_val_rf = mean_absolute_error(predicciones_val_rf, val_y)

print("MAE de validación para el modelo de Bosque Aleatorio: {:,.0f}".format(mae_val_rf))



#ejericio 2

# Crear un nuevo modelo de Random Forest para entrenar en todos los datos de entrenamiento
rf_model_on_full_data = RandomForestRegressor()

# Entrenar rf_model_on_full_data en todos los datos de entrenamiento
rf_model_on_full_data.fit(X, y)

# Imprimir un mensaje para indicar que el modelo ha sido entrenado
print("El modelo Random Forest ha sido entrenado en todos los datos de entrenamiento.")


#ejericio 3

# Leer el archivo de datos de prueba utilizando pandas
test_data = pd.read_csv("test.csv", index_col=0)

# Crear test_X que proviene de test_data pero solo incluye las columnas que usaste para las predicciones.
# La lista de columnas está almacenada en una variable llamada features
print(features)
test_X = test_data[features]
print(test_X)

# Hacer predicciones que enviaremos.
test_preds = rf_model_on_full_data.predict(test_X)

# Las líneas a continuación muestran cómo guardar las predicciones en el formato utilizado para la puntuación de la competición
# Solo tienes que descomentarlas.

output = pd.DataFrame({'Id': test_data.Id,
                       'SalePrice': test_preds})
output.to_csv('submission.csv', index=False)

# Imprimir el DataFrame 'output' que contiene las predicciones
print(output)

