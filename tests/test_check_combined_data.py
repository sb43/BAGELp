import BAGELp.staticMethods as sm
import pytest
import os, tempfile
import filecmp

'''
written test to check codebase integrity
of BAGELp
'''



class TestClass():
    pass

    def test_static_methods(self):
        testdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/')
        t_fcfile = testdir + 'test_fc.tsv'
        expected_outfile = testdir + 'bagelp.out'
        ess = testdir + '../../training_set/essential.txt'
        non_ess = testdir + '../../training_set/nonessential.txt'
        cpus = 1
        outdir=tempfile.mkdtemp(dir=".")
        columns=[1,2,3]
        # check input type function



        mystatic_obj = sm.StaticMthods()
        ess_list = mystatic_obj.load_signature_files(ess)
        noness_list = mystatic_obj.load_signature_files(non_ess)
        mystatic_obj.run_bagel(t_fcfile, ess_list, noness_list, cpus, column_list=columns,
                               NUM_BOOTSTRAPS=10, outfilename=outdir+'/bagelp.out')
        assert filecmp.cmp(expected_outfile, outdir+'/bagelp.out',
                           shallow=False), 'mageck out files are identical'

if __name__ == '__main__':
  mytests=TestClass()
  mytests()
