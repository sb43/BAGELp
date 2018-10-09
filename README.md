# BAGEL
Parallel version of bagel https://sourceforge.net/projects/bagel-for-knockout-screens/
BAGEL: software for Bayesian analysis of gene knockout screens using pooled library CRISPR or RNAi.

BAGEL is a Bayesian classifier for pooled library genetic perturbation screens, using either CRISPR-Cas9 or shRNA libraries. 
It uses training sets of known essential and nonessential genes to estimate what the fold change distribution of 
an essential or nonessential gene should look like. Then, for each uncharacterized gene, it takes all observations of 
reagents targeting that gene (guide RNA, for CRISPR-Cas9 screens, or short hairpin RNA) and makes a 
probabilistic statement about whether those observations were more likely drawn from the essential or nonessential training set.
A log2 Bayes Factor for each gene is reported.

