from week3_utility import *
from utilities import ToSingleLineOfString


def motif_enumeration_problem():
    k = 5
    d = 1
    dnas = ["CGTTACGGAAGTTAAGTATGGGTCG",
            "CGAAAAAGCCTCAGCTTAAACCCAA",
            "GCGTTCTCACCTATACGAAAAGGAA",
            "CGGAACTTCGAAAGACTATAGGTGT",
            "TTTCGTCATTCGTAAGGTGACCTCT",
            "CGCAATGGTGTTCATAAGCGCTTTT"]
    motifs = motif_enumeration(dnas, k, d)

    print ToSingleLineOfString(motifs)


def calculate_motif_entropy_scores():
    original = ["T   C   G   G   G   G   g   T   T   T   t   t",
                "c   C   G   G   t   G   A   c   T   T   a   C",
                "a   C   G   G   G   G   A   T   T   T   t   C",
                "T   t   G   G   G   G   A   c   T   T   t   t",
                "a   a   G   G   G   G   A   c   T   T   C   C",
                "T   t   G   G   G   G   A   c   T   T   C   C",
                "T   C   G   G   G   G   A   T   T   c   a   t",
                "T   C   G   G   G   G   A   T   T   c   C   t",
                "T   a   G   G   G   G   A   a   c   T   a   C",
                "T   C   G   G   G   t   A   T   a   a   C   C"]
    motifs = map(lambda s: s.upper(), map(lambda s: s.replace(' ', ''), original))
    #print ' '.join(map(lambda f: '%.4f' % f, score(motifs)))
    print str(sum(score(motifs)))


calculate_motif_entropy_scores()
