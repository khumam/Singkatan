import pandas as pd
import numpy as np
from os.path import exists


class SingkatanConverter:
    def __init__(self):
        self.dictionaryPath = './dict/singkatan.csv'
        self.dictionary = pd.DataFrame(np.array([]))
        self.processDictionary()

    def importDictionary(self, path):
        if not exists(path):
            raise Exception('Dictionary not found')

        self.dictionaryPath = path
        self.processDictionary()

    def processDictionary(self):
        data = pd.read_csv(self.dictionaryPath, sep=';', header=None)
        self.dictionary = pd.DataFrame(data)

    def convert(self, word):
        result = self.dictionary.loc[self.dictionary[0] == word]
        return result[1].tolist()[0].strip() if len(result) > 0 else word
