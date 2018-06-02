# Rafael Cartenet
# 2018

# Example on how to use stmvn.py

import numpy as np
from stmvn import mfcc_stmvn_smart_way
from stmvn import mfcc_stmvn_brute_way


# Let's say you have a MFCC matrix of size 13xN
N= 1000
MFCC_matrix= np.random.rand(N, 13)

mfcc1= mfcc_stmvn_smart_way(MFCC_matrix)
mfcc2= mfcc_stmvn_brute_way(MFCC_matrix)

print np.allclose(mfcc1, mfcc2, rtol=1e-10, atol=1e-10)
