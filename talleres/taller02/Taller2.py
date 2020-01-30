
def _euclides_(p,q):
     resto=p%q
     if resto==0:
         return q
     else :
         return _euclides_(q,p%q)
       
def _grupo_(indice,grupo,peso):
    if(indice==grupo.length):
        return peso==0
    else:
        return  _grupo_(indice+1,grupo,peso) or _grupo_(indice+1,grupo,peso-grupo[indice])
    
def _combinaciones_(cadena,n):  
    if cadena.length==0:
        print (n)
    else:
        combinaciones(n+cadena[0:-(cadena.length-1)], cadena[1])
	    combinaciones(n,cadena[1:])
def _ahorasi_ (cadena):
    return combinaciones(cadena,"")
    
    
    



        
     
     
 

        
         

