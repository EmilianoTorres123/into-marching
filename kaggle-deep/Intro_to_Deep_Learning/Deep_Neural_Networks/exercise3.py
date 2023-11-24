### YOUR CODE HERE: rewrite this to use activation layers
model = keras.Sequential([
    layers.Dense(units=32, input_shape=[8]),
    layers.Activation('relu'),
    layers.Dense(units=32),
    layers.Activation('relu'),
    layers.Dense(1),
])

# Check your answer
q_3.check()