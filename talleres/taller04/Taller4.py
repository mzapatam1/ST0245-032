import numpy


def _Punto1(A,n):
    max=A[n]
    if(n==0):
        max=A[0]
    if(n!=0):
        temp=numpy.amax(A,n-1) 
    if(temp>max):
        max=temp
    return(max)
    
def _grupo_(indice,grupo,peso):
    if(indice==grupo.length):
        return peso==0
    else:
        return  _grupo_(indice+1,grupo,peso) or _grupo_(indice+1,grupo,peso-grupo[indice])
        

    
    
