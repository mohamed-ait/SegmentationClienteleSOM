import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class SOM:
    def __init__(self, n_rows, n_cols, n_features, learning_rate=0.1, sigma=None):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n_features = n_features
        self.learning_rate = learning_rate
        self.sigma = sigma
        self.weights = np.random.rand(n_rows, n_cols, n_features)

    def _get_bmu(self, x):
        bmu_coords = None
        min_distance = float('inf')
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                distance = np.linalg.norm(x - self.weights[i, j])
                if distance < min_distance:
                    min_distance = distance
                    bmu_coords = (i, j)
        return bmu_coords

    def _decay_parameters(self, t):
        self.learning_rate = self.learning_rate * np.exp(-t / self.T)
        self.sigma = self.sigma * np.exp(-t / self.T)

    def _decay_parameters(self, t):
        self.learning_rate = self.learning_rate * np.exp(-t / self.T)
        self.sigma = self.sigma * np.exp(-t / self.T)

    def fit(self, X, T):
        self.T = T

        for t in range(T):
            x = X[np.random.choice(len(X))]
            bmu_coords = self._get_bmu(x)

            for i in range(self.n_rows):
                for j in range(self.n_cols):
                    distance = np.linalg.norm(np.array([i, j]) - np.array(bmu_coords))
                    theta = np.exp(-distance / (2 * self.sigma ** 2))
                    self.weights[i, j] = self.weights[i, j] + self.learning_rate * theta * (x - self.weights[i, j])

            self._decay_parameters(t)