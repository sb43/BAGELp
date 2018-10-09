from Bagel.formatInput import Bagel
import sys
import os
import argparse
import pkg_resources
import logging.config

configdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config/')
log_config = configdir + 'logging.conf'
logging.config.fileConfig(log_config)
log = logging.getLogger(__name__)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
version = pkg_resources.require("Bagel")[0].version


def main():  # pragma: no cover
    usage = "\n %prog [options] -f counts.tsv -l library.tsv"

    optParser = argparse.ArgumentParser(prog='BAGEL',
                                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    optional = optParser._action_groups.pop()
    required = optParser.add_argument_group('required arguments')

    required.add_argument("-i", "--fc_file", type=str, dest="fc_file", required=True,
                          default="", help="Tab-delmited file of sgRNA and fold changes.  See documentation for format.")

    required.add_argument("-e", "--ref_essential", type=str, dest="ref_essential", required=True,
                          help="File with list of training set of essential genes")

    required.add_argument("-c", "--col_list", type=str, dest="col_list", required=True,
                          help="list of data columns to be analysed")

    required.add_argument("-n", "--ref_non_essential", type=str, dest="ref_non_essential", required=True,
                          help="File with list of training set of nonessential genes")

    optional.add_argument("-N", "--numiter", type=int, dest="numiter", required=False,
                          default=1000, help="Number of bootstrap iterations for BAGEL (default 1000)")

    optional.add_argument("-np", "--num_processors", type=int, dest="num_processors", required=False,
                          default=1, help="Number of processors to use for parallel jobs")

    optional.add_argument("-o", "--outdir", type=str, dest="outdir",
                          default='./', help="path to output folder ")

    optional.add_argument("-v", "--version", action='version', version='%(prog)s ' + version)
    optional.add_argument("-q", "--quiet", action="store_false", dest="verbose", default=True)

    optParser._action_groups.append(optional)

    if len(sys.argv) == 1:
        optParser.print_help()
        log.debug("Missing one or more required arguments in the command, exiting......")
        sys.exit("Missing one or more required arguments in the command, exiting......")
    opts = optParser.parse_args()
    if not (opts.fc_file or opts.ref_essential or opts.ref_non_essential):
        log.debug('ERROR Arguments required \n Please run: pyCRISPRcleanR --help')
        sys.exit('\nERROR Arguments required\n\tPlease run: pyCRISPRcleanR --help\n')
    log.debug('Analysis started....')
    log.info(opts)
    mycrispr = Bagel(**vars(opts))
    mycrispr.run_analysis()


if __name__ == '__main__':
    main()
