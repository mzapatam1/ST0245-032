class Nodo():
    def __init__(self, objeto, siguiente = None):
        self.objeto = objeto
        self.siguiente = siguiente

class Lsimple():

    def __init__(self):
        self.primer_Nodo = None
        self.size = 0

    def contains(self,elemento):
        if self.size==0:
            return False
        else:
            nodoactual=self.primer_Nodo
            while nodoactual.siguiente != None:
                if elemento==nodoactual.objeto:
                    return True
                nodoactual = nodoactual.siguiente
            return False

    def insertion(self, i, dato):
        if self.size==0 and i==0:
            self.primer_Nodo=Nodo(dato)
        elif (self.size==0 and i!=0) or i>self.size:
                raise Exception ("No se puede insertar")
        else:
            nodoactual=self.primer_Nodo
            b=0
            while b<i:
                nodoactual=nodoactual.siguiente
                b+=1
            nodoactual.siguente=Nodo(dato,nodoactual.siguiente.siguiente)

def remove(self, i):
    if self.size==0 or i>self.size_:
        raise Exception("no se puede remover")
    else:
        nodo=self.primer_Nodo
        s=0
        while s<i:
            nodo=nodo.siguiente
            s+=1
        nodo.siguiente=nodo.siguiente.siguiente

#La complejidad no permite que este códogp sea un editor de texto, ya que es alta y se demoraría mucho más de lo deseable
#la complejidad de agregar n caracteres es O(n)        