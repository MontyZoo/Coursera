import unittest
from week2_utility import *

def ToString(array):
    return ' '.join([str(value) for value in array])

class TestSkew(unittest.TestCase):
    def test_sample(self):
        dna = 'CATGGGCATCGGCCATACGCC'
        skew_values = skew(dna)
        expected = '0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2'
        self.assertEqual(expected, ToString(skew_values))


class TestMinimumSkewProblem(unittest.TestCase):
    def test_sample(self):
        dna = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
        min_skew_indices = get_minimum_skews(dna)
        expected = '11 24'
        self.assertEqual(expected, ToString(min_skew_indices))

    def test_extra_dataset(self):
        with open('Datasets/MinimumSkewProblem_data01.txt', 'r') as datafile:
            dna = datafile.readline().strip()
        min_skew_indices = get_minimum_skews(dna)
        expected = '89969 89970 89971 90345 90346'
        self.assertEqual(expected, ToString(min_skew_indices))

    def test_dataset_01(self):
        """
        This dataset checks if your code's indexing is off.
        Specifically, it verifies that your code is not returning an index 1 too high (i.e. 4) or 1 too low (i.e. 2).
        """
        dna = 'ACCG'
        min_skew_indices = get_minimum_skews(dna)
        expected = '3'
        self.assertEqual(expected, ToString(min_skew_indices))

    def test_dataset_02(self):
        """
        This dataset checks to see if your code is missing the last symbol of Genome.
        """
        dna = 'ACCC'
        min_skew_indices = get_minimum_skews(dna)
        expected = '4'
        self.assertEqual(expected, ToString(min_skew_indices))

    def test_dataset_03(self):
        """
        This dataset makes sure you are not accidentally finding the maximum skew instead of the minimum skew.
        """
        dna = 'CCGGGT'
        min_skew_indices = get_minimum_skews(dna)
        expected = '2'
        self.assertEqual(expected, ToString(min_skew_indices))

    def test_dataset_04(self):
        """
        First, this dataset checks if you are only finding 1 index (and not multiple indices).
        Then, it checks if you are using a delimiter to separate your indices (ideally a space character).
        """
        dna = 'CCGGCCGG'
        min_skew_indices = get_minimum_skews(dna)
        expected = '2 6'
        self.assertEqual(expected, ToString(min_skew_indices))


class TestHammingDistance(unittest.TestCase):
    def test_sample(self):
        dna1 = 'GGGCCGTTGGT'
        dna2 = 'GGACCGTTGAC'
        hamming = get_hamming_distance(dna1, dna2)
        expected = 3
        self.assertEqual(expected, hamming)

    def test_dataset_01(self):
        dna1 = 'AAAA'
        dna2 = 'TTTT'
        hamming = get_hamming_distance(dna1, dna2)
        expected = 4
        self.assertEqual(expected, hamming)

    def test_dataset_02(self):
        dna1 = 'ACGTACGT'
        dna2 = 'TACGTACG'
        hamming = get_hamming_distance(dna1, dna2)
        expected = 8
        self.assertEqual(expected, hamming)

    def test_dataset_03(self):
        dna1 = 'ACGTACGT'
        dna2 = 'CCCCCCCC'
        hamming = get_hamming_distance(dna1, dna2)
        expected = 6
        self.assertEqual(expected, hamming)

    def test_dataset_04(self):
        dna1 = 'ACGTACGT'
        dna2 = 'TGCATGCA'
        hamming = get_hamming_distance(dna1, dna2)
        expected = 8
        self.assertEqual(expected, hamming)

    def test_dataset_05(self):
        dna1 = 'GATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGGTCACTAAATACT'
        dna2 = 'AATAGCAGCTTCTCAACTGGTTACCTCGTATGAGTAAATTAGGTCATTATTGACTCAGGTCACTAACGTCT'
        hamming = get_hamming_distance(dna1, dna2)
        expected = 15
        self.assertEqual(expected, hamming)

    def test_extra_dataset(self):
        with open('Datasets/HammingDistanceProblem_data01.txt', 'r') as datafile:
            datafile.readline()
            dna1 = datafile.readline().strip()
            dna2 = datafile.readline().strip()
            datafile.readline()
            expected = int(datafile.readline())
        hamming = get_hamming_distance(dna1, dna2)
        self.assertEqual(expected, hamming)


class TestApproximatePatternMatching(unittest.TestCase):
    def test_sample(self):
        pattern = 'ATTCTGGA'
        dna = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
        d = 3
        matching_positions = approximate_pattern_matching(pattern, dna, d)
        expected = '6 7 26 27'
        self.assertEqual(expected, ToString(matching_positions))

    def test_dataset_01(self):
        pattern = 'AAA'
        dna = 'TTTTTTAAATTTTAAATTTTTT'
        d = 2
        matching_positions = approximate_pattern_matching(pattern, dna, d)
        expected = '4 5 6 7 8 11 12 13 14 15'
        self.assertEqual(expected, ToString(matching_positions))

    def test_dataset_02(self):
        pattern = 'GAGCGCTGG'
        dna = 'GAGCGCTGGGTTAACTCGCTACTTCCCGACGAGCGCTGTGGCGCAAATTGGCGATGAAACTGCAGAGAGAACTGGTCATCCAACTGAATTCTCCCCGCTATCGCATTTTGATGCGCGCCGCGTCGATT'
        d = 2
        matching_positions = approximate_pattern_matching(pattern, dna, d)
        expected = '0 30 66'
        self.assertEqual(expected, ToString(matching_positions))

    def test_dataset_03(self):
        pattern = 'AATCCTTTCA'
        dna = 'CCAAATCCCCTCATGGCATGCATTCCCGCAGTATTTAATCCTTTCATTCTGCATATAAGTAGTGAAGGTATAGAAACCCGTTCAAGCCCGCAGCGGTAAAACCGAGAACCATGATGAATGCACGGCGATTGCGCCATAATCCAAACA'
        d = 3
        matching_positions = approximate_pattern_matching(pattern, dna, d)
        expected = '3 36 74 137'
        self.assertEqual(expected, ToString(matching_positions))

    def test_dataset_04(self):
        pattern = 'CCGTCATCC'
        dna = 'CCGTCATCCGTCATCCTCGCCACGTTGGCATGCATTCCGTCATCCCGTCAGGCATACTTCTGCATATAAGTACAAACATCCGTCATGTCAAAGGGAGCCCGCAGCGGTAAAACCGAGAACCATGATGAATGCACGGCGATTGC'
        d = 3
        matching_positions = approximate_pattern_matching(pattern, dna, d)
        expected = '0 7 36 44 48 72 79 112'
        self.assertEqual(expected, ToString(matching_positions))

    def test_dataset_05(self):
        pattern = 'TTT'
        dna = 'AAAAAA'
        d = 3
        matching_positions = approximate_pattern_matching(pattern, dna, d)
        expected = '0 1 2 3'
        self.assertEqual(expected, ToString(matching_positions))

    def test_dataset_06(self):
        pattern = 'CCA'
        dna = 'CCACCT'
        d = 0
        matching_positions = approximate_pattern_matching(pattern, dna, d)
        expected = '0'
        self.assertEqual(expected, ToString(matching_positions))

    def test_extra_dataset(self):
        with open('Datasets/ApproximatePatternMatchingProblem_data01.txt', 'r') as datafile:
            datafile.readline()
            pattern = datafile.readline().strip()
            dna = datafile.readline().strip()
            d = int(datafile.readline().strip())
            datafile.readline()
            expected = datafile.readline().strip()
        matching_positions = approximate_pattern_matching(pattern, dna, d)
        self.assertEqual(expected, ToString(matching_positions))


class TestApproximatePatternCount(unittest.TestCase):
    def test_sample(self):
        pattern = 'GAGG'
        dna = 'TTTAGAGCCTTCAGAGG'
        d = 2
        count = approximate_pattern_count(pattern, dna, d)
        expected = 4
        self.assertEqual(expected, count)

    def test_dataset_01(self):
        pattern = 'AA'
        dna = 'AAA'
        d = 0
        count = approximate_pattern_count(pattern, dna, d)
        expected = 2
        self.assertEqual(expected, count)

    def test_dataset_02(self):
        pattern = 'ATA'
        dna = 'ATA'
        d = 1
        count = approximate_pattern_count(pattern, dna, d)
        expected = 1
        self.assertEqual(expected, count)

    def test_extra_dataset(self):
        with open('Datasets/ApproximatePatternCount_data01.txt', 'r') as datafile:
            datafile.readline()
            pattern = datafile.readline().strip()
            dna = datafile.readline().strip()
            d = int(datafile.readline().strip())
            datafile.readline()
            expected = int(datafile.readline().strip())
        count = approximate_pattern_count(pattern, dna, d)
        self.assertEqual(expected, count)
