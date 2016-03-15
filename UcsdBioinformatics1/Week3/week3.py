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



motif_enumeration_problem()