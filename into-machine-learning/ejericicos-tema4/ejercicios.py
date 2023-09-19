import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressorr
from sklearn.model_selection import train_test_splitt
from sklearn.tree import DecisionTreeRegressor
home_data = pd.read_csv("train.csv", index_col=0)

#ejemplos-tema
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))


#ejercicios
candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
list_mae = []

# Supongamos que tienes una función get_mae(num_nodes, train_X, val_X, train_y, val_y) definida previamente

for num_nodes in candidate_max_leaf_nodes:
    result = get_mae(num_nodes, train_X, val_X, train_y, val_y)
    list_mae.append(result)

# Encuentra el mejor valor de max_leaf_nodes (será uno de los valores en la lista candidate_max_leaf_nodes)
best_tree_size = candidate_max_leaf_nodes[list_mae.index(min(list_mae))]

print("Mejor valor de max_leaf_nodes:", best_tree_size)


# Fill in argument to make optimal size and uncomment
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=0)

# Asumiendo que tienes tus datos en las variables X (características) y y (objetivo)
# fit the final model and uncomment the next two lines
final_model.fit(X, y)

print("Modelo de árbol de decisión final ajustado")






