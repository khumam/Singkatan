import pandas as pd
import numpy as np
from os.path import exists


class Singkatan:
    def __init__(self):
        self.dictionaryPath = ''
        self.dictionary = pd.DataFrame(np.array([]))

    def importDictionary(self, path):
        if not exists(path):
            raise Exception('Dictionary not found')

        self.dictionaryPath = path
        data = pd.read_csv(path, sep=';', header=None)
        self.dictionary = pd.DataFrame(data)

    def convert(self, word):
        for col, item in self.dictionary.iterrows():
            if word == item[0]:
                return item[1]
