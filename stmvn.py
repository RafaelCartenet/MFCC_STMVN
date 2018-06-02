# Rafael cartenet
# 2018

import numpy as np

def mfcc_stmvn_smart_way(MFCC_matrix, window_size=300):
    """ Short-time Mean and Variance Normalization
        According to paper:
        " Comparative evaluation of feature normalization techniques for voice
        password based speaker verification "
        - Md Jahangir Alam,
        - Pierre Ouellet,
        - Patrick Kenny,
        - Douglas O'Shaughnessy
    """

    # Initialize new mfcc matrix
    nb_frames, nb_coeffs= MFCC_matrix.shape
    new_MFCC_matrix= np.zeros(shape=(nb_frames, nb_coeffs))
    window= window_size//2

    # In order to compute mean and variance at time t in function of values at
    # t-1, we first compute the initial vectors mean and variance, at index t=m
    # Initialize mean and variance vectors
    mean= np.zeros(shape=(nb_coeffs))
    vari= np.zeros(shape=(nb_coeffs))

    t_s= 0
    t_e= min(nb_frames - 1, window)
    L= t_e - t_s + 1

    # Compute the first mean vector
    for j in range(t_s, t_e + 1):
        mean+= MFCC_matrix[j, :]
    mean/= L

    # Compute the first variance vector
    for j in range(t_s, t_e + 1):
        vari+= (MFCC_matrix[j, :] - mean)**2
    vari/= L

    # Compute new values of first MFCC vector, thanks to mean and variance
    new_MFCC_matrix[0, :]= (MFCC_matrix[0, :] - mean) / vari

    # We compute the following new vectors from the previous ones
    for m in range(1, nb_frames):
        t_s= max(0, m - window)
        t_e= min(nb_frames-1, m + window)
        L= t_e - t_s + 1

        if (m - window <= 0) and (m + window >= nb_frames):
            # Compute new values of first MFCC vector, thanks to mean and variance
            new_MFCC_matrix[m, :]= (MFCC_matrix[m, :] - mean) / vari
        else:
            if (m - window <= 0) and not (m + window >= nb_frames):
                ALPHA= MFCC_matrix[t_e, :]

                # Mean formula
                mean= ((L-1)*mean + ALPHA)/L

                # Variance formula
                vari= vari*(L-1)/L
                vari+= (ALPHA - mean)**2/(L-1)

            elif (m + window >= nb_frames) and not (m - window <= 0):
                BETA= MFCC_matrix[t_s - 1, :]

                # Mean formula
                mean= ((L+1)*mean - BETA)/L

                # Variance formula
                vari= vari*(L+1)/(L)
                vari-= (BETA - mean)**2/(L+1)

            else:
                ALPHA= MFCC_matrix[t_e, :]
                BETA= MFCC_matrix[t_s - 1, :]

                # Mean formula
                mean= (L*mean + ALPHA - BETA)/L

                # Variance formula
                vari= L*vari
                vari+= (ALPHA - BETA)**2/L
                vari+= (ALPHA - mean)**2
                vari-= (BETA - mean)**2
                vari/= L

            # Compute new values of first MFCC vector, thanks to mean and variance
            new_MFCC_matrix[m, :]= (MFCC_matrix[m, :] - mean) / vari

    return new_MFCC_matrix


def mfcc_stmvn_brute_way(MFCC_matrix, window_size=300):
    """ Short-time Mean and Variance Normalization
        According to paper:
        " Comparative evaluation of feature normalization techniques for voice
        password based speaker verification "
        - Md Jahangir Alam,
        - Pierre Ouellet,
        - Patrick Kenny,
        - Douglas O'Shaughnessy
    """

    # Initialize new mfcc matrix
    nb_frames, nb_coeffs= MFCC_matrix.shape
    new_MFCC_matrix= np.zeros(shape=(nb_frames, nb_coeffs))
    window= window_size//2

    for m in range(0, nb_frames):
        t_s= max(0, m - window)
        t_e= min(nb_frames-1, m + window)
        L= t_e - t_s + 1

        mean= np.zeros(shape=(nb_coeffs))
        vari= np.zeros(shape=(nb_coeffs))

        # compute mean vector
        for j in range(t_s, t_e + 1):
            mean+= MFCC_matrix[j, :]
        mean/= L

        # compute variance vector
        for j in range(t_s, t_e + 1):
            vari+= (MFCC_matrix[j, :] - mean)**2
        vari/= L

        # Compute new values of first MFCC vector, thanks to mean and variance
        new_MFCC_matrix[m, :]= (MFCC_matrix[m, :] - mean) / vari

    return new_MFCC_matrix
