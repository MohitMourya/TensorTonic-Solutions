import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Convert inputs to numpy arrays
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    # Number of samples and features
    N, D = X.shape

    # Initialize parameters
    w = np.zeros(D)
    b = 0.0

    # Gradient descent loop
    for _ in range(steps):

        # Linear combination
        z = X @ w + b

        # Predictions
        p = _sigmoid(z)

        # Error
        error = p - y

        # Gradients
        dw = (X.T @ error) / N
        db = np.sum(error) / N

        # Update parameters
        w -= lr * dw
        b -= lr * db

    return w, b
    