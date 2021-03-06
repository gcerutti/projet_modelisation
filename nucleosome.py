import numpy as np

class Histone(object):

    def __init__(self, state, nucleation):
        self.state = state
        self.nucleation = nucleation

    def __str__(self):
        return "Histone(S"+str(self.state)+("+N)" if self.nucleation else ")")

class Nucleosome(object):

    def __init__(self, n_histones=2):
        self.n_histones = n_histones
        self.histone_states = None
        self.histone_nucleations = None

        self.initialize()

    def __str__(self):
        return "".join([str(h)+" "  for h in self.histones]) 


    def initialize(self):
        self.histone_states = np.array([0 for h in range(self.n_histones)])
        self.histone_nucleations = np.array([0 for h in range(self.n_histones)])

