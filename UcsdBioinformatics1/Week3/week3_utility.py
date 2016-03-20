from Week2.week2_utility import get_neighbours
from Week1.week1_utility import increase_count
from collections import OrderedDict
from math import log

from utilities import ConvertBaseToIndex, ConvertIndexToBase


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


class Profile():
    def __init__(self):
        self._counts = [0] * 4
        self._probabilities = [0] * 4
        self.consensus = None
        self.entropy = None

    def add_base(self, base):
        index = ConvertBaseToIndex(base)
        self._counts[index] += 1

    def calculate_entropy(self):
        total = reduce(lambda a,b: a+b, self._counts)
        max = -1
        max_index = -1
        for index in range(4):
            self._probabilities[index] = float(self._counts[index]) / total
            if self._probabilities[index] > max:
                max = self._probabilities[index]
                max_index = index
        self.consensus = ConvertIndexToBase(max_index)
        temp = map(lambda p: p * log(p, 2) if p > 0 else 0, self._probabilities)
        self.entropy = sum(map(lambda p: p * log(p, 2) if p > 0 else 0, self._probabilities))
        if self.entropy < 0:
            self.entropy *= -1


def score(motifs):
    """
    Calculates the entropy score for a given list of motifs
    :param motifs: the list of motifs
    :return: the entropy score
    """
    motif_length = len(motifs[0])
    profiles = []
    for pos in range(motif_length):
        profile = Profile()
        profiles.append(profile)
        for motif in motifs:
            profile.add_base(motif[pos])
        profile.calculate_entropy()
    return map(lambda p: p.entropy, profiles)
