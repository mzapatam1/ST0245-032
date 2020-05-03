class Punto2:
    
    def __init__(self,size):
        self.size = size
        self.lista = [[] for i in range(size)]

    def addArc(self, source, destination):
        self.lista[source].append(destination)
        self.lista[destination].append(source)
        
    def isBicolorable(self, i):
      visited = [""]* self.size
      q = []
      q.append(i)
      visited[i] = "Blue"
      while( len(q) != 0):
        b = q.pop()
        for a in self.lista[b]:
          if(visited[a] == "" and visited[b] == "Blue"):
            q.append(a)
            visited[a] = "Red"
          if(visited[a] == "Red" and visited[b] == "Red"):
            print("IS NOT BICOLORABLE")
            return        
      print("IS COLORABLE") 
      
g = Punto2(3)
g.addArc(0, 1)
g.addArc(1,2)
g.addArc(2,0)
g.isBicolorable(0)
g2 = Punto2(3)
g2.addArc(0,1)
g2.addArc(1,2)
g2.isBicolorable(0)
g3 = Punto2(9)
g3.addArc(0,1)
g3.addArc(0,2)
g3.addArc(0,3)
g3.addArc(0,4)
g3.addArc(0,5)
g3.addArc(0,6)
g3.addArc(0,7)
g3.addArc(0,8)
g3.isBicolorable(0)

