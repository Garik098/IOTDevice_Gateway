import pickle

def pickle_out_data():
    pickle_out = open('config.pickle', 'rb')
    auth = pickle.load(pickle_out)
    pickle_out.close()
    return auth

def pickle_in_data(auth):
    pickle_in = open("config.pickle","wb")
    pickle.dump (auth, pickle_in)
    pickle_in.close()