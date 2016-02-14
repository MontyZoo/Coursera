from week2_utility import *
from week2_unit_tests import ToString


def skew_problem():
    dna = 'GAGCCACCGCGATA'
    skew_values = skew(dna)
    print ' '.join([str(value) for value in skew_values])


def minimum_skew_problem():
    with open('Datasets/MinimumSkewProblem_data02.txt', 'r') as datafile:
        dna = datafile.readline().strip()
    min_skew_indices = get_minimum_skews(dna)
    print ToString(min_skew_indices)


def hamming_distance_problem():
    with open('Datasets/HammingDistanceProblem_data02.txt', 'r') as datafile:
        dna1 = datafile.readline().strip()
        dna2 = datafile.readline().strip()
    hamming = get_hamming_distance(dna1, dna2)
    print hamming


def approximate_pattern_matching_problem():
    with open('Datasets/ApproximatePatternMatchingProblem_data02.txt', 'r') as datafile:
        pattern = datafile.readline().strip()
        dna = datafile.readline().strip()
        d = int(datafile.readline().strip())
    matching_positions = approximate_pattern_matching(pattern, dna, d)
    print ToString(matching_positions)


def count_approximate_pattern():
    pattern = 'AAAAA'
    dna = 'AACAAGCTGATAAACATTTAAAGAG'
    d = 2
    print approximate_pattern_count(pattern, dna, d)


def approximate_pattern_count_problem():
    with open('Datasets/ApproximatePatternCount_data02.txt', 'r') as datafile:
        pattern = datafile.readline().strip()
        dna = datafile.readline().strip()
        d = int(datafile.readline().strip())
    count = approximate_pattern_count(pattern, dna, d)
    print count


def frequent_words_with_mismatches_problem():
    with open('Datasets/FrequentWordsWithMismatchesProblem_data02.txt', 'r') as datafile:
        dna = datafile.readline().strip()
        params = datafile.readline().strip().split(' ')
        k = int(params[0])
        d = int(params[1])
    words = frequent_words_with_mismatches(dna, k, d)
    print ToString(words)


def frequent_words_with_mismatches_and_reverse_complements_problem():
    with open('Datasets/FrequentWordsWithMismatchesAndReverseComplementsProblem_data02.txt', 'r') as datafile:
        dna = datafile.readline().strip()
        params = datafile.readline().strip().split(' ')
        k = int(params[0])
        d = int(params[1])
    words = frequent_words_with_mismatches_and_reverse_complements(dna, k, d)
    print ToString(words)

frequent_words_with_mismatches_and_reverse_complements_problem()


def q2():
    dna1 = 'CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT'
    dna2 = 'CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG'
    hamming = get_hamming_distance(dna1, dna2)
    print hamming


def q3():
    print ToString(get_minimum_skews('CATTCCAGTACTTCGATGATGGCGTGAAGA'))


def q4():
    print str(approximate_pattern_count('CCC', 'CATGCCATTCGCATTGTCCCAGTGA', 2))


def q5():
    neighbours = frequent_words_with_mismatches('TGCAT', 5, 2)
    print len(neighbours)
