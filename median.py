"""
Pràctica Algorítmica 2019/2020
Participants:
    Víctor Alcobé
    Tibireu Paiu
    Dand Marbà
    Pau Agustí
"""
#to avoid recursion limit problems
import sys
sys.setrecursionlimit(10000)

class Median:
    """
    Class that countains methods and functions
    to calculate the median of every country
    """

    def __init__(self, data):
        self.data = data
        self.result = {}

    def median(self):
        """
        Class main method
        """
        self.sort(self.data, 0, len(self.data) - 1, "Geo_Location")
        self.lengths_for_country(self.data)
        self.calculate_median(self.result)

    def sort(self, sort_list, low, high, key):
        """
        Just quick sort algorith implemented for the sorter
        """

        if low < high:
            partition_index = partition(sort_list, low, high, key)
            self.sort(sort_list, low, partition_index-1, key)
            self.sort(sort_list, partition_index+1, high, key)

    def lengths_for_country(self, data):
        """
        Classificate lengths for country and sort them
        """

        count = 0
        for i in range(len(data)-1):
            count += 1
            self.result[data[i]["Geo_Location"]] = [count, 0, ""]

            if data[i]["Geo_Location"] != data[i+1]["Geo_Location"]:
                count = 0

            if i == len(data)-2:
                count += 1
                self.result[data[i]["Geo_Location"]] = [count, 0, ""]

        j = 0
        for row, item in self.result.items():
            self.sort(data, j, item[0]-1, "Length")
            j += item[0]

    def calculate_median(self, result):
        """
        Calculates the median of a sorted list
        """

        j = 0
        for row, item in result.items():
            if item[0] % 2 == 1:
                pointer = item[0] / 2
                item[1] = self.data[j+int(pointer)]["Length"]
                item[2] = self.data[j+int(pointer)]["Accession"]
            else:
                pointer = item[0] / 2
                med = (int(self.data[j+round(pointer)]["Length"]) + int(self.data[j+round(pointer-1)]["Length"]))/2
                item[1] = round(med)
                item[2] = self.data[j+int(pointer-1)]["Accession"]
            j += item[0]
            print(row, "-", item[1], "-", item[2])

def partition(sort_list, low, high, key):
    """
    Used on sort() not necessary to be a method, so implemented as function
    """

    i = (low -1)
    pivot = sort_list[high][key]
    for j in range(low, high):
        if sort_list[j][key] <= pivot:
            i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i+1], sort_list[high] = sort_list[high], sort_list[i+1]
    return i+1
