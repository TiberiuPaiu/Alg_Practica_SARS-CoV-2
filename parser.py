"""
Pràctica Algorítmica 2019/2020
Participants:
    Víctor Alcobé
    Tibireu Paiu
    Dand Marbà
    Pau Agustí
"""

import csv

class Parser:
    """
    Parser to read just the info we need
    """

    def __init__(self, inputfile):
        """
        geolocation_accessions_length: a list of three lists, one with the geoclocation,
        the other with accessions and the last one with the lengths

        countries: list of all the countries that appears on the database

        accessions: list of lists, first element of every list is the country,
        and all the others are the accessions
        """
        self.dades = []
        self.parse(inputfile)

    def parse(self, inputfile):
        """
        Read from the csv file the needed info
        """

        with open(inputfile, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                country = row['Geo_Location'].split(":")
                row['Geo_Location'] = country[0]
                self.dades.append(row)

def parser_fasta(fasta_file):
    """
    Extract the sequence of the Fasta files
    """

    with open("FASTA/"+fasta_file, "r") as file:
        sequence = ""
        line = file.readline()
        line = file.readline()

        while line:
            line = line.rstrip('\n')
            sequence += line
            line = file.readline()

    sequence = sequence[:100]
    return sequence
