import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

home_data = pd.read_csv("train.csv", index_col=0)

# Crear un modelo de Random Forest con un estado aleatorio fijo
rf_model = RandomForestRegressor(random_state=1)

# Entrenar el modelo con los datos de entrenamiento
rf_model.fit(train_X, train_y)

# Realizar predicciones en el conjunto de validación
rf_val_preds = rf_model.predict(val_X)

# Calcular el error absoluto medio (MAE) en el conjunto de validación
rf_val_mae = mean_absolute_error(val_y, rf_val_preds)

# Imprimir el MAE
print("Validation MAE for Random Forest Model: {:.2f}".format(rf_val_mae))


#ejemplo del tema 
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))


