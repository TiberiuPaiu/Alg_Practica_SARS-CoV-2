"""
Pràctica Algorítmica 2019/2020
Participants:
    Víctor Alcobé
    Tibireu Paiu
    Dand Marbà
    Pau Agustí
"""
import numpy

class NeedlemanWunsch:
    """
    This class generates the Needleman-Wunsch matrices
    and compute the coincidences of two sequences
    """

    def __init__(self, match=1, mismatch=0):
        self.match = match
        self.mismatch = mismatch
        self.matrix = []
        self.value_comparation = 0

    def matrix_generate(self, seq_1, seq_2):
        """
        Generates the NeedlemanWunsch matrix
        """
        #string to list
        seq_1 = list(seq_1)
        seq_2 = list(seq_2)

        matrix = numpy.full((len(seq_2) + 2, len(seq_1) + 2), ' ', dtype=object)
        matrix[0, 2:] = seq_1
        matrix[1, 1:] = 0
        matrix[2:, 0] = seq_2
        matrix[1:, 1] = 0
        self.matrix = matrix
        is_equal = {True: self.match, False: self.mismatch}

        for j in range(2, len(seq_1) + 2):
            for i in range(2, len(seq_2) + 2):
                self.matrix[i, j] = max(self.matrix[i - 1][j - 1] + is_equal[seq_1[j - 2] == seq_2[i - 2]],
                                        self.matrix[i - 1][j] ,
                                        self.matrix[i][j - 1] )
        if len(matrix) >= len(matrix[0]):
            self.value_comparation = (len(matrix) - 2) - self.matrix[i, j] 
        else:
            self.value_comparation = (len(matrix[0]) - 2) - self.matrix[i, j]

