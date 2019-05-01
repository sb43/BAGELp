# BAGELp
| Master                                              | Develop                                               |
| --------------------------------------------------- | ----------------------------------------------------- |
| [![Master Badge][travis-master-badge]][travis-repo] | [![Develop Badge][travis-develop-badge]][travis-repo] |

This is parallel implementation of original [BAGEL][BAGEL]: software for Bayesian analysis of gene knockout screens using pooled library CRISPR or RNAi.

BAGEL is a Bayesian classifier for pooled library genetic perturbation screens, using either CRISPR-Cas9 or shRNA libraries. 
It uses training sets of known essential and nonessential genes to estimate what the fold change distribution of 
an essential or nonessential gene should look like. Then, for each uncharacterized gene, it takes all observations 
of reagents targeting that gene (guide RNA, for CRISPR-Cas9 screens, or short hairpin RNA) and makes a probabilistic statement 
about whether those observations were more likely drawn from the essential or nonessential training set. A log2 Bayes Factor for each gene is reported.

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Design](#design)
- [Tools](#tools)
	- [BAGELp](#BAGELp)
	- [inputFormat](#inputformat)
	- [outputFormat](#outputformat)
- [INSTALL](#install)
	- [Package Dependencies](#package-dependencies)
- [Development environment](#development-environment)
	- [Development Dependencies](#development-dependencies)
		- [Setup VirtualEnv](#setup-virtualenv)
- [Cutting a release](#cutting-a-release)
	- [Install via `.whl` (wheel)](#install-via-whl-wheel)
- [Rererence](#reference)

<!-- /TOC -->

## Design
Uses python pool to parallelise bootstrapping step

## Tools

`BAGELp` has multiple commands, listed with `BAGELp --help`.

### BAGELp

Parallel implementation of original [BAGEL][BAGEL]

### inputFormat
Input is tab separated txt file (see example file in `tests/data/test_fc.txt`

Please refere original [BAGEL][BAGEL] for detailed file format [documentation][documentation]

### outputFormat

Calculates log2 Bayes Factor for each gene.

Please refere original  [BAGEL][BAGEL] for detailed file format [documentation][documentation]

## INSTALL
Installing via `pip install`. Simply execute with the path to the compiled 'whl' found on the [release page][BAGELp-releases]:

```bash
pip install BAGELp.X.X.X-py3-none-any.whl
```

Release `.whl` files are generated as part of the release process and can be found on the [release page][BAGELp-releases]

### Package Dependancies

`pip` will install the relevant dependancies, listed here for convenience, please refer requirements.txt for versions:
* [NumPy]
* [SciPy]

## Development environment

This project uses git pre-commit hooks.  As these will execute on your system it
is entirely up to you if you activate them.

If you want tests, coverage reports and lint-ing to automatically execute before
a commit you can activate them by running:

```
git config core.hooksPath git-hooks
```

Only a test failure will block a commit, lint-ing is not enforced (but please consider
following the guidance).

You can run the same checks manually without a commit by executing the following
in the base of the clone:

```bash
./run_tests.sh
```

### Development Dependencies

#### Setup VirtualEnv

```
cd $PROJECTROOT
hash virtualenv || pip3 install virtualenv
virtualenv -p python3 env
source env/bin/activate
python setup.py develop # so bin scripts can find module
```

For testing/coverage (`./run_tests.sh`)

```
source env/bin/activate # if not already in env
pip install pytest
pip install pytest-cov
```

__Also see__ [Package Dependancies](#package-dependancies)

### Cutting a release

__Make sure the version is incremented__ in `./setup.py`

### Install via `.whl` (wheel)

Generate `.whl`

```bash
source env/bin/activate # if not already
python setup.py bdist_wheel -d dist
```

Install .whl

```bash
# this creates an wheel archive which can be copied to a deployment location, e.g.
scp dist/BAGELp.X.X.X-py3-none-any.whl user@host:~/wheels
# on host
pip install --find-links=~/wheels BAGELp
```

### Reference
If using BAGELp please site
# URL of this repository and
# Hart T, Moffat J. BAGEL: a computational framework for identifying essential genes from pooled library screens. BMC Bioinformatics. 2016 Apr 16;17:164. doi:10.1186/s12859-016-1015-8.

<!--refs-->
 [NumPy]: http://www.numpy.org/
 [SciPy]: https://www.scipy.org
 [BAGEL]: https://sourceforge.net/projects/bagel-for-knockout-screens/
 [travis-master-badge]: https://travis-ci.org/sb43/BAGELp.svg?branch=master
 [travis-develop-badge]: https://travis-ci.org/sb43/BAGELp.svg?branch=develop
 [travis-repo]: https://travis-ci.org/sb43/BAGELp
 [BAGELp-releases]: https://github.com/sb43/BAGELp/releases
 [documentation]: https://sourceforge.net/p/bagel-for-knockout-screens/wiki/Home/#8fde
