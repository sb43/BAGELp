from abc import ABC, abstractmethod


class AbstractBagel(ABC):
    '''
      abstract class inilializes files to be comapred and implements two required methods
      to check user input and load config file
    '''

    def __init__(self, **kwargs):
        self.fcfile = kwargs['fc_file']
        self.ess = kwargs['ref_essential']
        self.noness = kwargs['ref_non_essential']
        self.column_list = kwargs['col_list']
        self.outdir = kwargs.get('outdir')
        self.cpus = kwargs.get('num_processors', 1)
        self.numiter = kwargs.get('numiter', 1000)
        super().__init__()

    @abstractmethod
    def check_input(self):
        pass
