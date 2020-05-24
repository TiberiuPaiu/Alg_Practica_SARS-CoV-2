#!/usr/bin/python3

"""
Pràctica Algorítmica 2019/2020
Participants:
    Víctor Alcobé
    Tibireu Paiu
    Dand Marbà
    Pau Agustí
"""

import sys
import urllib.request
from parser import Parser
from median import Median
from alignment import Alignment
from kmeans_clustering import Kmeans
import os ,shutil

def download_accessions(list_to_download):
    """
    Function that download all the accessions
    """
    count = 0
    if os.path.isdir("./FASTA"):
        shutil.rmtree("./FASTA")
        os.mkdir("./FASTA")
    else:
        os.mkdir("./FASTA")
    
    for country, dades in list_to_download.items():
        print("./FASTA/",country,"_",dades[2])
        id=dades[2]
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={0}&rettype=fasta".format(id)
        urllib.request.urlretrieve(url, "./FASTA/"+country+"_"+dades[2]+".fasta")

	


if __name__ == '__main__':
    PARSER = Parser(sys.argv[1])

    MEDIAN = Median(PARSER.dades)
    print("Median result for each country.")
    MEDIAN.median()
    
    print("Donwloading, please wait a minute.")
    download_accessions(MEDIAN.result)
    print("Downloaded Successfully.")

    print("Started the alignment of sequences. This will take some minutes, please wait.")
    ALIGNMENT = Alignment()
    ALIGNMENT.alignment()
    
    KMEANS = Kmeans(ALIGNMENT.alignment_result, 4, 300)
    KMEANS.kmeans()
    for i in range(len(KMEANS.clusters)):
    	print("----------------------------------------------------------")
    	for j in range(1,len(KMEANS.clusters[i])):
    	    	    	print("|",KMEANS.clusters[i][j],"|")
    print("----------------------------------------------------------")
    print("Ended the alignment of sequences.")
    #print(ALIGNMENT.alignment_result)
