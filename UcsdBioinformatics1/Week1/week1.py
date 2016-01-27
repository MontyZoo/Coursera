import utility
from utility_test import *


def q2():
    print utility.count_pattern('GACCATCAAAACTGATAAACTACTTAAAAATCAGT', 'AAA')


def q3():
    utility.get_most_freq_n_mer('CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA', 3)

def q4():
    print utility.get_reverse_complement('TTGTGTC')




test_count_5()
test_count_final()