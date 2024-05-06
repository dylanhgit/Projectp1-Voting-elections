import pickle
from os import path

def load_votes():
    if path.exists('votes.pkl'):
        with open('votes.pkl', 'rb') as file:
            return pickle.load(file)
    else:
        return {1: 0, 2: 0, 3: 0, 4: 0}

def save_votes(votes):
    with open('votes.pkl', 'wb') as file:
        pickle.dump(votes, file)

def load_voters():
    if path.exists('voters.pkl'):
        with open('voters.pkl', 'rb') as file:
            return pickle.load(file)
    return []

def save_voters(voters):
    with open('voters.pkl', 'wb') as file:
        pickle.dump(voters, file)
