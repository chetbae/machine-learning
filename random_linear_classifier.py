import numpy as np

def random_linear_classifier(D, k):
    r = np.random
    H = []
    err = []

    for j in range(k):
        theta = np.array([r.random(), r.random()])
        theta_0 = r.uniform(-1,1)
        H.append([theta, theta_0])
        err.append(int(training_error(D, theta, theta_0)))
    min_error = min(err)
    index = err.index(min_error)
    best_classifier = H[index]
    
    return best_classifier

def training_error(D, theta, theta_0) -> int:
    n = len(D)
    return 1/n * sum(1 if sign(D[i][0], theta, theta_0) != D[i][1] else 0 for i in range(n))

def sign(x, theta, theta_0):
    return 1 if np.dot(theta, x) + theta_0 > 0 else -1
