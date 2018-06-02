# Short-time Mean and Variance Normalization (STMVN)

STMVN applied to MFCC matrices.

This is my optimized implementation of a normalization from the paper:
https://www.crim.ca/perso/patrick.kenny/Jahangir_nolisp2011_16_final.pdf

---

The paper states:

*In the short-time mean and variance normalization (STMVN) technique, m-th frame
and k-th feature space C(m,k) are normalized as:*


![](images/Cstmvn.jpeg)

*where m and k represent the frame index and cepstral coefficients index,
respectively, L is the sliding window length in frames. μst(m,k) and σst(m,k) are the
short-time mean and standard deviation, respectively, defined as:*

![](images/MUst.jpeg)

![](images/SIGMAst.jpeg)

---
