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



approximate_pattern_count_problem()

