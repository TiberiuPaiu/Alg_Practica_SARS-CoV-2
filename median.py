"""
Pràctica Algorítmica 2019/2020
Participants:
    Víctor Alcobé
    Tibireu Paiu
    Dand Marbà
    Pau Agustí
"""
class Median:
	"""
	Class that contains methods and functions
	to calculate the median of every country
	"""

	def __init__(self, dades):
  
		self.dades = dades
		self.result = {}
		
	def median(self):
		self.sort(self.dades, 0, len(self.dades) - 1, "Geo_Location")
		self.n_porpais(self.dades)
		self.calculate_median(self.result)
			
	def sort(self, sort_list, low, high,key):
		#Just quick sort algorith implemented for the sorter

    		if low < high:
        		pi = partition(sort_list, low, high,key)
        		self.sort(sort_list, low, pi-1,key)
        		self.sort(sort_list, pi+1, high,key)
		
	def n_porpais(self,dades):
		
		#Contar por cada pais quantos son del mismo i guadar quantos para poder hacer la mediana. Una ver agrupados todos los paises oredenar por su Length
		

		cont=0;
		for i in range(len(dades)-1):		
			cont+=1
			self.result[dades[i]["Geo_Location"]]=[cont,0,""]

			if dades[i]["Geo_Location"] != dades[i+1]["Geo_Location"]:
				suma=0
				cont=0
		
			if i == len(dades)-2  :
				cont+=1
				self.result[dades[i]["Geo_Location"]]=[cont,0,""]
		
		j=0;
		for row, v in self.result.items():
			self.sort(dades, j, v[0]-1,"Length")
			j+=v[0]
			
	
	def calculate_median(self,result):
		"""
		Calculates the median of a sorted list
		"""

		j=0;c=0;
		for row, v in result.items():
		
			if v[0] % 2 == 1:
				aputa=v[0] / 2
				v[1]=self.dades[j+int(aputa)]["Length"]
				v[2]=self.dades[j+int(aputa)]["Accession"]
			else:
				aputa=v[0] / 2
				r=(int(self.dades[j+round(aputa)]["Length"]) + int(self.dades[j+round(aputa-1)]["Length"]) )/2
				v[1]=round(r)
				v[2]=self.dades[j+int(aputa-1)]["Accession"]
			
			j+=v[0]
			c+=1
			print(row,"-",v[1],"-",v[2] )
		
		
	
def partition(sort_list, low, high ,key):
	"""
	Used on quick_sort() not necessary to be a method, so implemented as function
	"""
	
	i = (low -1)
	pivot = sort_list[high][key]
	for j in range(low, high):
		if sort_list[j][key] <= pivot:
			i += 1
			sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
	sort_list[i+1],sort_list[high] = sort_list[high], sort_list[i+1]
	return (i+1)	
