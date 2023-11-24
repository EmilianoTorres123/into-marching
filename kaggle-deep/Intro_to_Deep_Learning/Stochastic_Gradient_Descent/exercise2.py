# YOUR CODE HERE
history = model.fit(
    X, y,
    validation_data=(X, y),
    batch_size=128,
    epochs=200,
)

# Check your answer
q_2.check()