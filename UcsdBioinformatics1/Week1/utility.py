import sys

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