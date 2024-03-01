# Taken from https://github.com/c o m f y a n o n y m o u s / C o m f y U I
# This file is only for reference, and not used in the backend or runtime.


import pickle

load = pickle.load

class Empty:
    pass

class Unpickler(pickle.Unpickler):
    def find_class(self, module, name):
        #TODO: safe unpickle
        if module.startswith("pytorch_lightning"):
            return Empty
        return super().find_class(module, name)
