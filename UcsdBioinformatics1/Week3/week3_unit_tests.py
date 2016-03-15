import unittest
from week3_utility import *
from Week2.week2_unit_tests import ResultEqual

class TestMotifEnumeration(unittest.TestCase):
    def test_sample(self):
        k = 3
        d = 1
        dnas = ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]
        motifs = motif_enumeration(dnas, k, d)
        expected = "ATA ATT GTT TTT"

        self.assertTrue(ResultEqual(expected, motifs))

    def test_dataset_1(self):
        k = 3
        d = 0
        dnas = ["ACGT", "ACGT", "ACGT"]
        motifs = motif_enumeration(dnas, k, d)
        expected = "ACG CGT"

        self.assertTrue(ResultEqual(expected, motifs))

    def test_dataset_2(self):
        k = 3
        d = 1
        dnas = ["AAAAA", "AAAAA", "AAAAA"]
        motifs = motif_enumeration(dnas, k, d)
        expected = "AAA AAC AAG AAT ACA AGA ATA CAA GAA TAA"

        self.assertTrue(ResultEqual(expected, motifs))

    def test_dataset_2_2(self):
        k = 3
        d = 0
        dnas = ["AAAAA", "AAAAA", "AAAAA"]
        motifs = motif_enumeration(dnas, k, d)
        expected = "AAA"

        self.assertTrue(ResultEqual(expected, motifs))

    def test_dataset_3(self):
        k = 3
        d = 3
        dnas = ["AAAAA", "AAAAA", "AAAAA"]
        motifs = motif_enumeration(dnas, k, d)
        expected = "AAA AAC AAG AAT ACA ACC ACG ACT AGA AGC AGG AGT ATA ATC ATG ATT CAA CAC CAG CAT CCA CCC CCG CCT CGA CGC CGG CGT CTA CTC CTG CTT GAA GAC GAG GAT GCA GCC GCG GCT GGA GGC GGG GGT GTA GTC GTG GTT TAA TAC TAG TAT TCA TCC TCG TCT TGA TGC TGG TGT TTA TTC TTG TTT"

        self.assertTrue(ResultEqual(expected, motifs))

    def test_dataset_4(self):
        k = 3
        d = 0
        dnas = ["AAAAA", "AAAAA", "AACAA"]
        motifs = motif_enumeration(dnas, k, d)
        expected = ""

        self.assertTrue(ResultEqual(expected, motifs))

    def test_dataset_5(self):
        k = 3
        d = 0
        dnas = ["AACAA", "AAAAA", "AAAAA"]
        motifs = motif_enumeration(dnas, k, d)
        expected = ""

        self.assertTrue(ResultEqual(expected, motifs))



