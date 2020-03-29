import csv
def read_Dataset(filename):
    data = []
    with open(filename, encoding='utf-8') as datos:
        read = csv.reader(datos, delimiter=";")
        for line in read:
            data.append(line)
        return(data)   
    
    
    
    

