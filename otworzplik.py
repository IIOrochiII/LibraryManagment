import pickle
with open('ocena.data', 'rb') as f:
    data = pickle.load(f)
    print(data)