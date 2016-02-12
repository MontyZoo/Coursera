
def skew(dna):
    values = [0]
    for nucleotide in dna:
        value = values[-1]
        if nucleotide == 'C':
            value -= 1
        elif nucleotide == 'G':
            value += 1
        values.append(value)
    return values


def get_minimum_skews(dna):
    """
    Find a position in a genome where the skew diagram attains a minimum.
    :param dna: A DNA string Genome.
    :return: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).
    """
    skew_values = skew(dna)
    min_value_indices = []
    min_value = 1000000
    for index in range(len(dna)+1):
        value = skew_values[index]
        if value < min_value:
            min_value_indices = [index]
            min_value = value
        elif value == min_value:
            min_value_indices.append(index)
    return min_value_indices


def get_maximum_skews(dna):
    """
    Find a position in a genome where the skew diagram attains a maximum.
    :param dna: A DNA string Genome.
    :return: All integer(s) i maxmizing Skewi (Genome) among all values of i (from 0 to |Genome|).
    """
    skew_values = skew(dna)
    max_value_indices = []
    max_value = -1000000
    for index in range(len(dna)+1):
        value = skew_values[index]
        if value > max_value:
            max_value_indices = [index]
            max_value = value
        elif value == max_value:
            max_value_indices.append(index)
    return max_value_indices


def get_hamming_distance(dna1, dna2):
    """
    Hamming Distance Problem: Compute the Hamming distance between two strings.
        Input: Two strings of equal length.
    :return: The Hamming distance between these strings.
    """
    if len(dna1) != len(dna2):
        raise Exception("The two DNA strings must have equal length.")

    hamming_distance = 0
    for index in range(len(dna1)):
        if dna1[index] != dna2[index]:
            hamming_distance += 1
    return hamming_distance


def approximate_pattern_matching(pattern, dna, mismatches):
    """
    Find all approximate occurrences of a pattern in a string.
    :param pattern: the k-mer pattern string
    :param dna: the DNA string where pattern is searched against
    :param mismatches: the maximum hamming distance allowed for a match
    :return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
    """
    pattern_len = len(pattern)
    matches = []
    for index in range(len(dna)-pattern_len+1):
        sub_dna = dna[index:index+pattern_len]
        hamming_distance = 0
        is_match = True
        for i in range(pattern_len):
            if pattern[i] != sub_dna[i]:
                hamming_distance += 1
                if hamming_distance > mismatches:
                    is_match = False
                    break
        if is_match:
            matches.append(index)
    return matches


def approximate_pattern_count(pattern, dna, mismatches):
    """
    Count occurrences of k-mers, possibly with mismatches.
    :param pattern: the k-mer pattern string
    :param dna: the DNA string where pattern is searched against
    :param mismatches: the maximum hamming distance allowed for a match
    :return: Count occurrence of Pattern appears as a substring of a DNA with at most d mismatches.
    """
    return len(approximate_pattern_matching(pattern, dna, mismatches))
