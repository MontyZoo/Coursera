from Week2.week2_utility import get_neighbours
from Week1.week1_utility import increase_count
from collections import OrderedDict


def _find_motifs(dna, k, d):
    """
    Find all (k, d)-motifs in a dna string
    :param dna: the dna string
    :param k: k-mer
    :param d: the maximally allowed distance for a match
    :return: All (k, d)-motifs in Dna
    """
    motifs = set()
    for index in range(len(dna)-k+1):
        motif = dna[index: index+k]
        neighbours = get_neighbours(motif, d)
        for neighbour in neighbours:
            motifs.add(neighbour)
    return motifs


def motif_enumeration(dnas, k, d):
    """
    Find all (k, d)-motifs in a list of dna strings
    :param dna: the dna string
    :param k: k-mer
    :param d: the maximally allowed distance for a match
    :return: All (k, d)-motifs in Dna
    """

    '''
    motifs = set()
    for dna in dnas:
        motifs = motifs.union(_find_motifs(dna, k, d))
    return motifs
    '''

    motifs = []
    for dna in dnas:
        motifs.append(_find_motifs(dna, k, d))
    from operator import and_
    return reduce(and_, motifs)

