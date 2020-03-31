class Punto1():
    
    def __init__(self):
       self.tabla = [0]*10
       
    def funcion_hash(self, k):
       return int(k[0]) % 10
       
    def get(self, k):
       k=self.funcion_hash[k]
       return self.tabla[k]
       
    def put(self, k, v): 
       k=self.funcion_hash[k]
       self.tabla[k]=v
       
       
class Punto2():
    def __init__(self):
       self.tabla = [0]*4
       
    def funcion_hash(self, k):
       return int(k[0]) % 4
            
    def put(self, k): 
        if(k=="Google):
            v="Estados Unidos"
        if(k=="La locura"):
            v="Colombia"
        if(k=="Nokia"):
            v="Finlandia"
        if(k=="Sony"):
            v="Japon"
            
       k=self.funcion_hash[k]
       self.tabla[k]=v
    
        
    

