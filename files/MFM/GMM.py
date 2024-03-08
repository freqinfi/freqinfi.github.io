from elice_utils import EliceUtils
import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
from scipy.special import logsumexp

elice_utils = EliceUtils()


def plt_show():
    plt.savefig("fig")
    elice_utils.send_image("fig.png")

class GMM:

    def __init__(self, n_components=2, max_iter=100, tol=1e-4):
        self.n_components = n_components
        self.max_iter = max_iter
        self.tol = tol
        # Code your initializations here. 
        self.weights_ = None
        self.means_ = None
        self.covariances_ = None
    
    def fit(self, X):
        n_samples, n_features = X.shape
        
        # 1. Initialization
        self.weights_ = np.ones(self.n_components) / self.n_components

        # Select a random idx as initialization target
        random_idx = np.random.choice(X.shape[0], self.n_components, replace=False)
        self.means_ = X[random_idx, :]  # Set one of the random cluster as the mean 

        # Set covariance. Highly recommend you to set rowvar=False.
        self.covariances_ = [np.cov(X, rowvar=False)] * self.n_components
        
        log_likelihood = 0

        for _ in range(self.max_iter):

            # 2. E-Step
            responsibilities = self._e_step(X)

            # 3. M-Step
            self._m_step(X, responsibilities)

            # Check convergence. If the new likelihood exceeds the tolerance, break the loop.
            # Use L1 norm for distance computation.
            new_log_likelihood = self._compute_log_likelihood(X)

            if np.abs(new_log_likelihood - log_likelihood) < self.tol:

                break

            log_likelihood = new_log_likelihood

    def _e_step(self, X):

        n_components=self.n_components

        responsibilities = np.zeros((X.shape[0], n_components))
    
        for i in range(self.n_components):
            # For each responsibility component in the component, update the responsibility based on gaussian pdf. 
            # Responsibility is the adaptively weighted gaussian pdfs based on each component. 

            rv = multivariate_normal(mean=self.means_[i], cov=self.covariances_[i])  # Assuming mean and cov are available
            responsibilities[:, i] = rv.pdf(X) * self.weights_[i]

        # Normalize the responsibilities
        responsibilities_sum = np.sum(responsibilities, axis=1, keepdims=True)
        responsibilities /= responsibilities_sum

        return responsibilities
    
    def _m_step(self, X, responsibilities):

        N = X.shape[0]

        for i in range(self.n_components):

            # weights for each component?
            weight = np.sum(responsibilities[:,i])/N
            
            # Update means
            self.means_[i] = np.sum(responsibilities[:, i].reshape(-1, 1) * X, axis=0) / np.sum(responsibilities[:, i])
        
            # Update covariances
            covariance = (X - self.means_[i]).T @ (responsibilities[:, i].reshape(-1, 1) * (X - self.means_[i])) / np.sum(responsibilities[:, i])
            self.covariances_[i] = covariance
        
            # Update weights
            self.weights_[i] = weight
            
    
    def _compute_log_likelihood(self, X):

        log_likelihood = np.zeros((X.shape[0], self.n_components))

        for i in range(self.n_components):

            distribution = multivariate_normal(mean=self.means_[i], cov=self.covariances_[i])
            log_likelihood[:, i] = np.log(distribution.pdf(X) * self.weights_[i])

        final_likelihood = np.sum(logsumexp(log_likelihood, axis=1))

        return final_likelihood

    def predict(self, X):

        responsibilities = self._e_step(X)
        cluster_idx = np.argmax(responsibilities, axis=1)
        return cluster_idx

    

def main():

    np.random.seed(42)
    cluster_1 = np.random.multivariate_normal([2, 2], [[1, 0.5], [0.5, 1]], 200)
    cluster_2 = np.random.multivariate_normal([8, 8], [[1, -0.6], [-0.6, 1]], 200)
    cluster_3 = np.random.multivariate_normal([4, 8], [[1, 0.6], [0.6, 1]], 200)

    data_combined = np.vstack((cluster_1, cluster_2, cluster_3))

    # Fit the GMM
    gmm = GMM(n_components=3)
    gmm.fit(data_combined)

    # Predict cluster assignments
    labels = gmm.predict(data_combined)

    # Visualize the results
    plt.figure(figsize=(10, 6))
    plt.scatter(data_combined[:, 0], data_combined[:, 1], c=labels, edgecolors='w', cmap=plt.cm.get_cmap('viridis', 3))
    plt.colorbar()
    plt.title("GMM Clustering of Synthetic 2D Data")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt_show()
    

if __name__ == "__main__":
    main()
