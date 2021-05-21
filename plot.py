from typing import List
import matplotlib.pyplot as plt
import numpy as np
from random_dataset_gen import random_dataset_gen
from random_linear_classifier import random_linear_classifier

def plot(training_dataset, h):
    # plotting points
    pos = [[],[]]
    neg = [[],[]]

    for x, y in training_dataset:
        if y == 1:
            pos[0].append(x[0])
            pos[1].append(x[1])
        else:
            neg[0].append(x[0])
            neg[1].append(x[1])
            
    plt.scatter(pos[0],pos[1],marker="+")
    plt.scatter(neg[0],neg[1],marker="_")
    
    #
    x = np.linspace(-1,1,100)
    y = -(1/h[0][0]) * x + h[0][1]
    plt.plot(x,y, 'b')

    #normal vector
    plt.arrow(0,0, h[0][1], h[0][0])

    plt.grid(True)
    plt.xlim([-1,1])
    plt.ylim([-1,1])
    plt.axhline(0,color='black')
    plt.axvline(0,color='black')
    plt.show()

def main():
    D = random_dataset_gen(10, seed=69)
    h = random_linear_classifier(D, 100)
    plot(D, h)

if __name__ == "__main__":
    main()