from elice_utils import EliceUtils
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from collections import Counter

elice_utils = EliceUtils()

def plt_show():
    plt.savefig("fig")
    elice_utils.send_image("fig.png")

class KNNClassifier:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):

        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):

        distances = []
        for x_train in self.X_train:
            distances.append(np.linalg.norm(x - x_train))

        k_indices = np.argsort(distances)[:self.k]

        k_nearest_labels = []
        for i in k_indices:
            k_nearest_labels.append(self.y_train[i])

        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

class NaiveBayesClassifier:

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self._classes = np.unique(y)
        n_classes = len(self._classes)

        print(n_samples, n_features)

        # each class have mean, var
        self._mean = np.zeros((n_classes, n_features), dtype=np.float64)
        self._var = np.zeros((n_classes, n_features), dtype=np.float64)
        self._priors = np.zeros(n_classes, dtype=np.float64)

        # prior : 전체 sample에서 해당 class의 확률
        for c in self._classes:
            X_c = X[y==c]
            self._mean[c] = X_c.mean(axis=0)
            self._var[c] = X_c.var(axis=0)
            self._priors[c] = X_c.shape[0] / float(n_samples)

    def predict(self, X):
        
        y_pred = [self._predict(x) for x in X]

        return np.array(y_pred)

    def _predict(self, x):

        # founding class that have maximum posterior

        posteriors = []
        
        for idx, c in enumerate(self._classes):
            prior = np.log(self._priors[idx]) # For each class, compute the log prior
            class_conditional = np.sum(np.log(self._pdf(idx, x))) # Sum of log pdf(likelihood)
            
            # each feature, calculate prob and multiply all these probabilities

            # in log, poduct -> plus
            posterior = prior + class_conditional
            posteriors.append(posterior)

        # using arg_max -> finding idx that have max_posterior
        max_posterior_idx = np.argmax(posteriors)

        return self._classes[max_posterior_idx]

    def _pdf(self, class_idx, x):
        mean = self._mean[class_idx]
        var = self._var[class_idx]

        gaussian_pdf = (1 / (np.sqrt(2 * np.pi * var))) * np.exp(-((x - mean) ** 2) / (2 * var))

        # Return gaussian pdf
        return gaussian_pdf

def main():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Fit the KNN Classifier
    knn = KNNClassifier(k=3)
    knn.fit(X_train, y_train)
    knn_predictions = knn.predict(X_test)

    # Fit the Naive Bayes classifier
    nb = NaiveBayesClassifier()
    nb.fit(X_train, y_train)
    nb_predictions = nb.predict(X_test)

    knn_accuracy = np.mean(knn_predictions == y_test)
    print(f"KNN Accuracy: {knn_accuracy * 100:.2f}%")

    nb_accuracy = np.mean(nb_predictions == y_test)
    print(f"Naive Bayes Accuracy: {nb_accuracy * 100:.2f}%")

    # Visualize the KNN results using the first two features
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test[:, 0], X_test[:, 1], c=knn_predictions, edgecolors='w', cmap=plt.cm.get_cmap('viridis', 3))
    plt.colorbar()
    plt.title("KNN Classifier Clustering on Iris Data (first two features)")
    plt.xlabel(iris.feature_names[0])
    plt.ylabel(iris.feature_names[1])
    plt.grid(True)
    plt_show()

    # Visualize the Naive Bayes results using the first two features
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test[:, 0], X_test[:, 1], c=nb_predictions, edgecolors='w', cmap=plt.cm.get_cmap('viridis', 3))
    plt.colorbar()
    plt.title("Naive Bayes Classifier Clustering on Iris Data (first two features)")
    plt.xlabel(iris.feature_names[0])
    plt.ylabel(iris.feature_names[1])
    plt.grid(True)
    plt_show()

if __name__ == "__main__":
    main()
