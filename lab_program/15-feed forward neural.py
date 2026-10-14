import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Feedforward neural network class
class FeedforwardNeuralNetwork:
    def __init__(self, input_size, hidden_size, output        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.biases_hidden = np.random.rand(hidden_size)
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        self.biases_output = np.random.rand(output_size)

    def forward(self, X):
        # Hidden layer
        hidden_input = np.dot(X, self.weights_input_hidden) + self.biases_hidden
        hidden_output = sigmoid(hidden_input)

        # Output layer
        output_input = np.dot(hidden_output, self.weights_hidden_output) + self.biases_output
        output_output = sigmoid(output_input)

        return output_output

# Example usage
if __name__ == "__main__":
    # Input data (X) and labels (y)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Create a neural network with 2 input neurons, 2 hidden neurons, 1 output neuron
    nn = FeedforwardNeuralNetwork(input_size=2, hidden_size=2, output_size=1)

    # Predict
    predictions = nn.forward(X)
    print("Predictions:")
    print(predictions)
