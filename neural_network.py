import numpy as np

class NeuralNetwork:
    def __init__(self, input_size=3, hidden_size=4, output_size=1):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        self.W1 = np.random.randn(self.hidden_size, self.input_size)
        self.b1 = np.random.randn(self.hidden_size, 1)
        self.W2 = np.random.randn(self.output_size, self.hidden_size)
        self.b2 = np.random.randn(self.output_size, 1)

    def predict(self, inputs):
        inputs = np.array(inputs).reshape(-1, 1)
        hidden = np.tanh(np.dot(self.W1, inputs) + self.b1)
        output = self.sigmoid(np.dot(self.W2, hidden) + self.b2)
        return output[0][0] > 0.5  # прыжок или нет

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def copy(self):
        clone = NeuralNetwork(self.input_size, self.hidden_size, self.output_size)
        clone.W1 = np.copy(self.W1)
        clone.b1 = np.copy(self.b1)
        clone.W2 = np.copy(self.W2)
        clone.b2 = np.copy(self.b2)
        return clone

    def mutate(self, rate):
        def mutate_matrix(matrix):
            mutation = np.random.randn(*matrix.shape) * rate
            matrix += mutation

        mutate_matrix(self.W1)
        mutate_matrix(self.b1)
        mutate_matrix(self.W2)
        mutate_matrix(self.b2)
