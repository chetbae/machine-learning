import numpy as np

def random_dataset_gen(N: int, seed=17):
    # seed
    rng = np.random.default_rng(seed)

    # generate values
    def r(): return rng.uniform(-1,1)
    def bin(): return rng.choice([-1,1])

    # training dataset (x(x1,x2),y{-1 or +1})
    training_dataset = [[np.array([r(), r()]), bin()] for i in range(N)]
    #print(training_dataset)
    return training_dataset

if __name__ == "__main__":
    random_dataset_gen(3)