import csv
import sys

class Parser:

    def __init__(self, inputfile):
        """
        accessions_geo_location: two lists, the one have the accession and the
                                other the country which it belongs

        countries: list of all the countries that appears on the database

        accessions: list of lists, first element of every list is the country,
                    and all the others are the accessions
        """
        self.accessions_geo_location = [[], []]
        self.countries = []
        self.accessions = []
        self.parse(inputfile)
        self.convert_accessions()
        self.cut_countries()

    def parse(self, inputfile):

        """ Read from the csv file the needed info"""

        with open(inputfile, newline = '') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                country = row['Geo_Location'].split(":")
                country = country[0]

                if country not in self.countries:
                    self.countries.append(country)

                self.accessions_geo_location[1].append(row['Accession'])
                self.accessions_geo_location[0].append(country)

        self.countries = list(filter(None, self.countries))
        self.accessions = self.countries

    def cut_countries(self):

        """ Split accessions and classfied into countries.
            Returns a list of lists, first element of every list
            is the country, and all the others are accessions"""

        for index_accession in range(len(self.accessions_geo_location[0])):
            for index_countries in range(len(self.countries)):
                if self.countries[index_countries] == self.accessions_geo_location[0][index_accession]:
                    self.accessions[index_countries].append(self.accessions_geo_location[1][index_accession])


        #print(self.accessions)
        #print(self.countries)

    def convert_accessions(self):

        """ Used to convert a list into a list of lists needed for the append
            of the cut_countries() function"""

        result = []
        for element in self.accessions:
            temp = element.split(', ')
            result.append(temp)

        self.accessions = result

#if __name__ == '__main__':
    #parser = Parser(sys.argv[1])
