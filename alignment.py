"""
Pràctica Algorítmica 2019/2020
Participants:
    Víctor Alcobé
    Tibireu Paiu
    Dand Marbà
    Pau Agustí
"""

from os import listdir
from parser import parser_fasta
from needlemanwunsch import NeedlemanWunsch

class Alignment:
    """
    Class that contains methods and functions
    to realize the alignment of sequences
    """

    def __init__(self):

        self.alignment_result = []

    def alignment(self):
        """
        Alignment of sequences main function
        """
        explored = []
        files_list = listdir("FASTA/")
        for first_file in files_list:
            for second_file in files_list:
                if second_file not in explored:
                    if first_file != second_file:
                        self.extract_sequence(first_file, second_file)
            explored.append(first_file)

    def extract_sequence(self, file_1, file_2):
        """
        Extract the sequence of the Fasta files
        with the function of parser.py
        """

        sequence_1 = parser_fasta(file_1)
        sequence_2 = parser_fasta(file_2)

        coincidences = alignment_of_sequences(sequence_1, sequence_2)
        files = [""+file_1+" - "+file_2]
        files.append(coincidences)
        self.alignment_result.append(files)



def alignment_of_sequences(sequence_1, sequence_2):
    """
    Alignment of the sequences with a value return
    This value is the max length of min sequence - coincidences
    So the min value is the best
    And the max value is the worst
    """
    n_w = NeedlemanWunsch()
    n_w.matrix_generate(sequence_1, sequence_2)
    coincidences = n_w.value_comparation
    return coincidences
