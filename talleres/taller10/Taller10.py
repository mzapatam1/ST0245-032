class Nodo:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def __init__(self):
      self.root = None
    
def insertar(self, data):
    if self.root is None:
      self.root = Nodo(data)             
    else:
      self.__insertar_aux(data, self.root)  
      
def __insertar_aux(self, data, actual):
      if(actual.right is None or actual.left is None):
          
        if(data > actual.data):
          actual.right = Nodo(data)
        else:
          actual.left = Nodo(data)
       
      else:
          
        if(data > actual.data):
            self.__insertar_aux(data, actual.right)
        else:
            self.__insertar_aux(data, actual.left)
      return actual
             
def buscar(self, data):
      return self.__buscar_aux(data, self.root) 

def __buscar_aux(self, data, actual):
      if(actual is None):
          return False
      else:
          if(data == actual.data):
              return True
          else:
              if(data > actual.data):
                  return self.__buscar_aux(data, actual.right)
              else:
                  return self.__buscar_aux(data, actual.left)
              
#La complejidad del algoritmo anterior es de O(log n)


