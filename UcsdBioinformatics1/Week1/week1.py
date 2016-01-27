import utility


def q2():
    print str.count('GACCATCAAAACTGATAAACTACTTAAAAATCAGT', 'AAA')


def q3():
    utility.get_most_freq_n_mer('CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA', 3)

print utility.get_reverse_complement('TTGTGTC')