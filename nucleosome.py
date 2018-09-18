class Nucleosome(object):

    def __init__(self, n_histones=2):
        self.n_histones = n_histones
        self.histones = None

        self.initialize()

    def __str__(self):
        return "".join([str(h)+" "  for h in self.histones]) 

    def initialize(self):
        self.histones = [[0,0] for h in range(self.n_histones)]
