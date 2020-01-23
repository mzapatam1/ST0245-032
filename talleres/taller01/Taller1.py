import math 
class Punto1:
   
    def _init_(self, x, y):
        self.x=x
        self.y=y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def radio_polar(self):
        return math.sqrt(self.x**2 + self.y**2) 
    def angulo_polar(self):
        return  math.atan(self.x/self.y)
    def dist_euclidiana(self, other):
        return abs(math.sqrt((self.x-other.x)**2+(self.y-other.y)**2))
    
class Punto2:
    def _init_(self, day, month, year):
        self.day= day
        self.month=month
        self.year=year
    def get_day(self):
        return self.day
    def get_month(self):
        return self.month
    def get_year(self):
        return self.year
    def obt_cadena(self):
        return self.day + '/'+self.month+'/' + self.year
    def mayor(self, other):
        if self.year > other.year:
            return "1"
        elif other.year > self.year:
            return "-1"
        elif self.month > other.month:
            return "1"
        elif other.month > self.month:
            return "-1"
        elif self.day > other.day:
            return "1"
        elif other.day > self.day:
            return "-1"
        else:
            return "0"
class Punto3:
    
    def _init_(self,id):
        self.id=id
        
    def incrementar(self):
        
        self.id= self.id + 1
       
       
    def incrementos(self):
        return self.id
    def toString(self):
        return "El valor final de id es: "+ self.id 
        
        
        
        
    
    
        
    
    
        
            
    
    
    
    
    
  
        
