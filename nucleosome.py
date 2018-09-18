import numpy as np

class Nucleosome(object):

    def __init__(self, n_histones=2):
        self.n_histones = n_histones
        self.histones = None

        self.initialize()

    def initialize(self):
        self.histones = np.array([[0,0] for h in range(self.n_histones)])
