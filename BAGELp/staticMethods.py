import sys
import tarfile
import numpy as np
import logging
from . import parallel

log = logging.getLogger(__name__)


class StaticMthods(object):
    """ Static methosds for common tasks """

    def __init__(self):
        super().__init__()

    def input_checker(infile):
        """
          checks user input file and returns it's type
        """
        try:
            if tarfile.is_tarfile(infile):
                log.info(("input is an archive:", infile))
                return 'tar'
            else:
                log.info(("input is a file:", infile))
                return 'file'
        except IsADirectoryError:
            return 'dir'
        except IOError as ioe:
            sys.exit('Error in reading input file:{}'.format(ioe.args[0]))

    # ------------------------------Analysis methods---------------------------------

    @staticmethod
    def load_signature_files(sig_file):
        """
        :param sig_dir_path:
        :return: signature_dict
        """
        signature_dict = {}
        signature = None
        try:
            with open(sig_file) as f:
                gene_list = f.read().splitlines()
        except IOError:
            log.error("Unable to load reference_genes file:" + sig_file)
        return gene_list

    @staticmethod
    def run_bagel(fc_file, Ess, nonEss, cpus, column_list=[], NUM_BOOTSTRAPS=1000, outfilename='./bagel_out'):
        """
        :param fc_file: file containing crispr foldchange data as defined in BAGEL documentation
        :param Ess: essential genes
        :param nonEss: non essential genes
        :param cpus: num of cpus
        :param column_list: columns to analyse [see BAGEL documentation]
        :param NUM_BOOTSTRAPS: number of bootstrap iterations
        :param outfilename: output file
        :return:  return on success
        """
        bf = parallel.run_parallel_bagel(fc_file, column_list, Ess, nonEss,
                                         cpus, NUM_BOOTSTRAPS=NUM_BOOTSTRAPS)
        fout = open(outfilename, 'w')
        fout.write('GENE\tBF\tSTD\tNumObs\n')
        for g in sorted(bf.keys()):
            if bf[g]:  # sb43 added to avoid empty array error
                num_obs = len(bf[g])
                bf_mean = np.mean(bf[g])
                bf_std = np.std(bf[g])
                fout.write('{0:s}\t{1:4.3f}\t{2:4.3f}\t{3:d}\n'.format(g, bf_mean, bf_std, num_obs))
        fout.close()
        return 0
