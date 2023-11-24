from tensorflow.keras import callbacks
from tensorflow.keras.callbacks import EarlyStopping

# YOUR CODE HERE: define an early stopping callback
early_stopping = EarlyStopping(
    min_delta=0.001, # minimium amount of change to count as an improvement
    patience=5, # how many epochs to wait before stopping
    restore_best_weights=True,
)

# Check your answer
q_3.check()