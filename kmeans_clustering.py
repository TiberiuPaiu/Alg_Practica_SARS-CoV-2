"""
Pràctica Algorítmica 2019/2020
Participants:
    Víctor Alcobé
    Tibireu Paiu
    Dand Marbà
    Pau Agustí
"""

import random

class Kmeans:
    """
    Implemented KMenas Clustering
    """
    def __init__(self, inputdata, k, iterations):
        """
        data: results of alignament comparasion of all the sequences
        k: number of cluster we want to classify our data
        iterations: num iterations we want for the algorithm to found
                    a good solution
        clusters: list of clusters
        min, max: minimum and maximum value of our inputdata
        """
        self.data = inputdata
        self.k = k
        self.iterations = iterations
        self.clusters = []
        self.min = 0
        self.max = len(self.data) 

    def search_max_min(self):
        """
        Method to search the max and min value of our inputdata
        to random generate our cluster between those margins
        """
        for sample in self.data:
            if sample[1] < self.min:
                self.min = sample[1]
            if sample[1] > self.max:
                self.max = sample[1]

    def generate_clusters(self):
        """
        Generating randomly our clusters between min and max
        """
        for _ in range(self.k - 1):
            cluster = [self.data[random.randint(0, len(self.data) - 1 )][1]]
            self.clusters.append(cluster)

    def compute_clusters(self):
        """
        Compute the clusters for every iteration
        """
        cluster = []
        for index in range(len(self.clusters)):
            total_sum = 0
            total_len = len(self.clusters[index]) - 1
            if total_len < 1:
                break
            for sample in self.clusters[index][1:]:
                total_sum = total_sum + int(sample[1])

            new_cluster = int(total_sum / total_len)
            cluster.append([new_cluster])
        self.clusters = cluster

    def kmeans(self):
        """
        Kmeans algorithm
        """
        self.search_max_min()
        self.generate_clusters()

        for _ in range(self.iterations):
            for sample in self.data:
                cluster = self.clusters
                index = self.min_distance(sample[1])
                cluster[index].append(sample)
            self.clusters = cluster
            self.compute_clusters()
        self.clusters = cluster


    def min_distance(self, sample):
        """
        Minium distance from sample to cluster
        """
        #max length of sequence will be 10000 so isnt a problem
        min_dist = 10000
        index_min = 1
        for index in range(len(self.clusters)):
            dist = abs(self.clusters[index][0] - sample)
            if dist < min_dist:
                index_min = index
                min_dist = dist

        return index_min
