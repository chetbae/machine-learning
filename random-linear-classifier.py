import matplotlib.pyplot as plt
import numpy as np

# seed
rng = np.random.default_rng(17)

# generate values
def r(): return rng.uniform(-1,1)
def bin(): return rng.choice([-1,1])
def h(): return [[r(),r()],r()]

# training dataset (x(x1,x2),y{-1 or +1})
N = 10
training_dataset = [[[r(),r()], bin()] for i in range(N)]




# plotting points
pos = [[],[]]
neg = [[],[]]

for i in range(N):
    x0,x1,y = training_dataset[i][0][0], training_dataset[i][0][1], training_dataset[i][1]
    if y == 1:
        pos[0].append(x0)
        pos[1].append(x1)
    else:
        neg[0].append(x0)
        neg[1].append(x1)
        
plt.scatter(pos[0],pos[1],marker="+")
plt.scatter(neg[0],neg[1],marker="_")

plt.grid(True)
plt.xlim([-1,1])
plt.ylim([-1,1])
plt.axhline(0,color='red')
plt.axvline(0,color='red')
plt.show()

def random_linear_classifier(D, k, d):
    for j in range(k):
        x = 0
