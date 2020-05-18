import sys
import csv
import os.path
import urllib.request
directorio="muestras"
archiu="sequences.csv"
con_archiu=[]
dic_mediana={}
mostra1=""
mostra2=""

def ller_csv(archiu_csv):
	with open(archiu_csv) as File:
		reader = csv.DictReader(File)
		for row in reader:
			con_archiu.append(row)
		

def coprobar_csv(archiu_csv):

	if os.path.exists(archiu_csv):
		ller_csv(archiu_csv)
	else:
		print ("La ruta no existe :",archiu_csv)	

def mostra_patalla(lista, *claves):
	
	if  len(claves) == 0:
		i=0
		for d in lista:
			i+=1
			print (i,"",end="")
			for key, value in d.items():
		    		print (key,"->",value," \t",end="")
			print ("\n")
	else:
		i=0
		for key in lista:
			i+=1
			print (i,"",end="")
			for j in range(len(claves)):  
				print (claves[j],"->",key[claves[j]]," \t",end="")
			print ("\n")
			
			
def mediana():
	cont=0;
	## conta el numero maximo de quatos paises son i guardar el numero maximo por cada pais.
	for i in range(len(con_archiu)-1):		
		cont+=1
		dic_mediana[con_archiu[i]["Geo_Location"]]=[cont,0,""]

		if con_archiu[i]["Geo_Location"] != con_archiu[i+1]["Geo_Location"]:
			suma=0
			cont=0
		
		if i == len(con_archiu)-2  :
			cont+=1
			dic_mediana[con_archiu[i]["Geo_Location"]]=[cont,0,""]

	## hacer la mediana por conjutos 	
	j=0;c=0;
	for row, v in dic_mediana.items():
		
		if v[0] % 2 == 1:
			aputa=v[0] / 2
			v[1]=con_archiu[j+int(aputa)]["Length"]
			v[2]=con_archiu[j+int(aputa)]["Accession"]
		else:
			aputa=v[0] / 2
			r=(int(con_archiu[j+round(aputa)]["Length"]) + int(con_archiu[j+round(aputa-1)]["Length"]) )/2
			v[1]=round(r)
			v[2]=con_archiu[j+int(aputa-1)]["Accession"]
			
			
		j+=v[0]
		c+=1  
		print(c,"-",row,"-",v[1],"-",v[2] )

def partition(sort_list, low, high):
    i = (low -1)
    pivot = sort_list[high]["Geo_Location"]
    for j in range(low, high):
        if sort_list[j]["Geo_Location"] <= pivot:
            i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i+1],sort_list[high] = sort_list[high], sort_list[i+1]
    return (i+1)
            
def div_veceras(sort_list, low, high):
    if low < high:
        pi = partition(sort_list, low, high)
        div_veceras(sort_list, low, pi-1)
        div_veceras(sort_list, pi+1, high)
	
def main(): 
	if len(sys.argv) == 2:
		coprobar_csv(sys.argv[1]+"/sequences.csv")
	else:
		coprobar_csv(directorio+"/"+archiu)

	mostra_patalla(con_archiu,"Geo_Location","Length")
	print ("\n")
	div_veceras(con_archiu, 0, len(con_archiu) - 1)
	mostra_patalla(con_archiu,"Geo_Location","Length")
	mediana()
	Genotype
	print ("Mostra 1 :")
	mostra1 = input() 
	urllib.request.urlretrieve("https://www.ncbi.nlm.nih.gov/nuccore/"+mostra1+"?report=fasta")
	print ("Mostra 2 :")
	mostra2 = input()
	
main()
