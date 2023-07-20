
import csv

with open("14_Archivos_CSV\\datos.csv")as archivoCSV:
    #print(csv.reader(archivoCSV))
    
    """ O """
    
    #reader = csv.reader(archivoCSV)
    #print(reader)
    
    reader = csv.reader(archivoCSV)
    for row in reader:
        print(row)
        
