import sys
import csv
import os.path

directorio="muestras"
archiu="sequences.csv"
con_archiu=[]

def ller_csv(archiu_csv):
	with open(archiu_csv) as File:
		reader = csv.DictReader(File)
		for row in reader:
			con_archiu.append(row)
		

def coprobar_csv(archiu_csv):

	if os.path.exists(archiu_csv):
		ller_csv(archiu_csv)
	else:
		print ("El fichero no existe :",archiu_csv)	

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
			
			
def mediana(lista):
	dic_result = {}
	suma=0;
	cont=0;
	for i in range(len(lista)-1):		
		suma+=int(lista[i]["Length"])
		cont+=1
		dic_result[lista[i]["Geo_Location"]]=[cont,suma,0]

		if lista[i]["Geo_Location"] != lista[i+1]["Geo_Location"]:
			suma=0
			cont=0
		
		if i == len(lista)-2  :
			suma+=int(lista[i+1]["Length"])
			cont+=1
			dic_result[lista[i]["Geo_Location"]]=[cont,suma,0]
	

	for row, v in dic_result.items():
		v[2]=v[1] / v[0]
		print(row,"-",v[2] )
				
	
def main(): 
	if len(sys.argv) == 2:
		coprobar_csv(sys.argv[1]+"/sequences.csv")
	else:
		coprobar_csv(directorio+"/"+archiu)
	
	mostra_patalla(con_archiu,"Geo_Location","Length")
	sorted_list = sorted(con_archiu, key=lambda item: item["Geo_Location"])
	print ("\n")
	mostra_patalla(sorted_list,"Geo_Location","Length")
	mediana(sorted_list)

main()
