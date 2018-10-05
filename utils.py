import pickle
from collections import defaultdict


def warm_start(overwrite=False):
    if overwrite:
        db = defaultdict(str)
        db['[1990] Partitioning Sparse Matrices with Eigenvectors of Graphs.pdf'] = 'Reinforcement Learning'
        with open('db.p', 'wb') as g:
            pickle.dump(db, g)

        with open('db.p', 'rb') as f:
            db = pickle.load(f)
            print(db)


warm_start(overwrite=False)

