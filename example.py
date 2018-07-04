# Rafael Cartenet
# 2018

# Example on how to use stmvn.py

# imports
import time
import numpy as np
from stmvn import mfcc_stmvn_smart_way
from stmvn import mfcc_stmvn_brute_way


# Let's say you have a MFCC matrix of size 13xN
N= 1000
MFCC_matrix= np.random.rand(N, 13)


# Accuracy comparisons
mfcc1= mfcc_stmvn_smart_way(MFCC_matrix)
mfcc2= mfcc_stmvn_brute_way(MFCC_matrix)

print np.array_equal(mfcc1, mfcc2)
print np.mean(mfcc1 - mfcc2)
print np.allclose(mfcc1, mfcc2, rtol=1e-10, atol=1e-10)


# Complexity comparisons
N= 1000
brute_avg_time= 0
smart_avg_time= 0
nb_samples= 100
for _ in range(nb_samples):
    MFCC_matrix= np.random.rand(N, 13)

    t0= time.time()
    mfcc1= mfcc_stmvn_smart_way(MFCC_matrix)
    smart_avg_time+= time.time() - t0

    t0= time.time()
    mfcc2= mfcc_stmvn_brute_way(MFCC_matrix)
    brute_avg_time+= time.time() - t0

smart_avg_time/= nb_samples
brute_avg_time/= nb_samples

print smart_avg_time
print brute_avg_time


# \mu(m+1, k)=  \mu(m, k) +  \frac{1}{L}C(m+\frac{L}{2},k) + (-\frac{1}{L}C(m-\frac{L}{2},k)
