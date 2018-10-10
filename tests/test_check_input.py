import BAGELp.formatInput as fc
import pytest
import os

'''
written test to check codebase integrity
of archCompare
'''

class TestClass():
    testdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/')
    t_fcfile = testdir + 'test_fc.tsv'
    ess = testdir + '../../training_set/essential.txt'
    non_ess = testdir + '../../training_set/nonessential.txt'

    cwdpath = os.getcwd()

    def test_file_input(self):
        # check input type function
        my_files=fc.Bagel(fc_file=self.t_fcfile, ref_essential=self.ess, ref_non_essential=self.non_ess, col_list="1,2,3")
        assert ['file','file','file'] == my_files.check_input(),'input files test OK'

if __name__ == '__main__':
  mytests=TestClass()
  mytests()
