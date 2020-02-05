def HannoiAux(n,origen,intermedio,destino):
    if n == 1:
        print("mover el disco desde ",origen,"hasta ",destino)
    else:
        HannoiAux(n-1,origen,destino,intermedio)
        print("mover el disco desde ",origen,"hasta ",destino)
        HannoiAux(n-1,intermedio,origen,destino)

def Hannoi(n):
    HannoiAux(n,1,2,3)

Hannoi(7)

def permutationsAux(base,s):
    if(len(s) == 0):
        print(base)
    else:
        for i in range (len(s)):
            permutationsAux(base+s[i],s[0:i]+s[i+1:]) 
            
def permutations(s):
    permutationsAux("",s)
    
permutations("abc")
        
            