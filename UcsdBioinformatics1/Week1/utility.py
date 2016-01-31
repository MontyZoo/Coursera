# coding=utf-8
import sys

"""
    PatternCount(Text, Pattern)
        count ← 0
        for i ← 0 to |Text| − |Pattern|
            if Text(i, |Pattern|) = Pattern
                count ← count + 1
        return count
"""
def count_pattern(dna, pattern):
    dna = dna.upper()
    pattern = pattern.upper()
    count = 0
    start = 0
    while True:
        start = dna.find(pattern, start) + 1
        if start > 0:
            count += 1
        else:
            return count

"""
    FrequentWords(Text, k)
        FrequentPatterns ← an empty set
        for i ← 0 to |Text| − k
            Pattern ← the k-mer Text(i, k)
            Count(i) ← PatternCount(Text, Pattern)
        maxCount ← maximum value in array Count
        for i ← 0 to |Text| − k
            if Count(i) = maxCount
                add Text(i, k) to FrequentPatterns
        return FrequentPatterns
"""
def get_most_freq_n_mer(dna, n):
    dna = str.upper(dna)
    length = str.__len__(dna)
    dict = {}
    for index in range(0, length-n):
        n_mer = dna[index: index + n]
        if dict.__contains__(n_mer):
            dict[n_mer] += 1
        else:
            dict[n_mer] = 1

    max_count = 0
    most_freq_n_mers = []
    for n_mer, count in dict.iteritems():
        if count > max_count:
            most_freq_n_mers = [n_mer]
            max_count = count
        elif count == max_count:
            most_freq_n_mers.append(n_mer)

    print 'Most Frequent n-mer Count: %d' % max_count
    for n_mer in most_freq_n_mers:
        print n_mer
    return most_freq_n_mers, max_count


def get_reverse_complement(dna):
    dna = str.upper(dna)
    complement = ''
    for base in dna:
        if base == 'A':
            complement += 'T'
        elif base == 'T':
            complement += 'A'
        elif base == 'C':
            complement += 'G'
        elif base == 'G':
            complement += 'C'
        else:
            raise Exception('Invalid DNA base.')
    return complement[::-1]