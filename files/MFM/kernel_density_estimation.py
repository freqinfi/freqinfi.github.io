import math
from elice_utils import EliceUtils
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from collections import defaultdict
elice_utils = EliceUtils()

def plt_show():
    plt.savefig("fig")
    elice_utils.send_image("fig.png")

# class point(test set)에서 분류한 후에 이를 이용하여 Kernel density estimation을 이용하여
# 각 class에 존재할 확률을 구한 뒤 가장 높은 확률을 가진 class로 classify한다.

class GaussianKDEParzenWindow:
    def __init__(self, bandwidth=1.0):
        self.bandwidth = bandwidth
        self.data = None
    
    def gaussian_kernel(self, u):

        # print("here!")
        # print(u.shape)
        d = u.shape[0]

        function_val = (1 / ((2 * np.pi)**(d/2))) * np.exp(-0.5 * (np.dot(u.T,u)))

        return function_val

    def fit(self, data):
        self.data = np.array(data)
    
    def evaluate(self, x):

        N = self.data.shape[0]
        x = np.array(x)

        # print("here")
        # print(x.shape)

        d = x.shape[0]
        h = self.bandwidth
        
        density = 0

        for data_point in self.data:

            density += self.gaussian_kernel((x - data_point)/self.bandwidth)

        prob = density / (N*(h**d))

        return prob
    
    def __call__(self, x):
        return self.evaluate(x)

class KDEClassifier:

    def __init__(self, bandwidth=1.0):

        self.bandwidth = bandwidth
        self.kde_by_class = defaultdict(GaussianKDEParzenWindow)
    
    def fit(self, X, y):

        #print("here")
        #print(X)
        #print(y)

        # extract class type
        self.classes = np.unique(y)

        # in each class
        for c in self.classes:

            X_class = X[y == c]
            print(X_class)

            kde = GaussianKDEParzenWindow(bandwidth=self.bandwidth)
            kde.fit(X_class)
            self.kde_by_class[c] = kde
    
    def predict(self, X):

        # each x, compare with all class
        predicted_classes = []

        for x in X:
            
            max_prob = -1
            predicted_class = None
            for c, kde in self.kde_by_class.items():

                prob = kde(x)
                # finding class that have max prob 
                if prob > max_prob:
                    max_prob = prob
                    predicted_class = c

            predicted_classes.append(predicted_class)

        return np.array(predicted_classes)

def main():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Fit the KDE Classifier
    clf = KDEClassifier(bandwidth=0.5)
    clf.fit(X_train, y_train)

    # Predict class assignments
    y_pred = clf.predict(X_test)

    accuracy = np.mean(y_pred == y_test)
    print(f"Accuracy: {accuracy * 100:.2f}%")

    # Visualize the results using the first two features
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, edgecolors='w', cmap=plt.cm.get_cmap('viridis', 3))
    plt.colorbar()
    plt.title("KDE Classifier Clustering on Iris Data (first two features)")
    plt.xlabel(iris.feature_names[0])
    plt.ylabel(iris.feature_names[1])
    plt.grid(True)
    plt_show()
    


if __name__ == "__main__":
   main()



