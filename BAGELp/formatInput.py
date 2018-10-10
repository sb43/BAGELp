import logging
import os
import sys
from BAGELp.abstractBagel import AbstractBagel
from BAGELp.staticMethods import StaticMthods as SM

log = logging.getLogger(__name__)

'''
  This code run's Francesco's CRISPRcleanR algorithm implementation in python
'''


class Bagel(AbstractBagel):
    """
        Main class , loads user defined parameters and files
    """

    def check_input(self):
        """
           check input type and presence of user supplied
           input files
        """
        super().check_input()
        input_type = []
        for infile in (self.fcfile, self.ess, self.noness):
            input_type.append(SM.input_checker(infile))
        return input_type

    def run_analysis(self):
        """
          method to run the analysis
        """
        cpus = self.cpus
        outdir = self.outdir
        fcfile = self.fcfile
        iter = self.numiter
        columns = self.column_list.split(',')
        column_list = [int(c) for c in columns]

        if outdir:
            os.makedirs(outdir, exist_ok=True)
        # check input files
        (input1, input2, input3) = self.check_input()

        if input1 and input2:
            ess = SM.load_signature_files(self.ess)
            noness = SM.load_signature_files(self.noness)
            SM.run_bagel(fcfile, ess, noness, cpus,
                         column_list=column_list, NUM_BOOTSTRAPS=iter,
                         outfilename=outdir + '/bagelp.out')
            log.info(" BAGEL Analysis completed successfully.....")
        else:
            sys.exit('Input data is not in required format, see inputFormat in README file')
