class Nodo():
    def __init__(self,valor):
        self.valor=valor
        self.der=None
        self.izq=None

    def organizar(self,valor):
        if self.valor:
            if valor<self.valor:
                if self.izq is None:
                    self.izq=Nodo(valor)
                else:
                    self.izq.organizar(valor)
            elif valor>self.valor:
                if self.der is None:
                    self.der=Nodo(valor)
                else:
                    self.der.organizar(valor)
        else:
            self.valor=valor

def imprimir(Nodo):
    if Nodo is not None:
        imprimir(Nodo.izq)
        imprimir(Nodo.der)
        print(Nodo.valor)
        

lista=[50,30,24,5,28,45,98,52,60]
tree=Nodo(lista[0])

for i in range(1,len(lista)):
    tree.organizar(lista[i])

imprimir(tree) 


