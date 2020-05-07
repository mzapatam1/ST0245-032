class Graph: 
    def __init__(self,size):
        self.size = size
        self.graph = [[] for i in range(size)]
        
    def addArc(self, source, destination):
        self.graph[source].append(destination)
        self.graph[destination].append(source)


    def AuxIsReachableBFS(self, s, d): 
         visited =[False]*(self.size) 
         queue=[] 
         queue.append(s) 
         visited[s] = True
   
         while queue:
              n = queue.pop(0) 
              if n == d: 
                  return True;

              for i in self.graph[n]: 
                  if visited[i] == False: 
                      queue.append(i) 
                      visited[i] = True
         return False;
     
    def IsReachableDFS(self, s, d):
      visited = [False] * self.size 
      self.DFSaux(s,d, visited)
       
        
    
    
    def DFSaux(self, s, d, visited):
      visited[s] = True
      for a in self.graph[s]:
        if(not visited[a]):
          if(a == d):
             print("SÍ")
            
          self.DFSaux(a, d, visited)
      

     
  
     
def IsReachableBFS(g, s, d):
    if g. AuxIsReachableBFS(s, d):
        print("SÍ")
    else:
        print("NO")
        
     

    
g = Graph(4) 
g.addArc(0, 1) 
g.addArc(0, 2) 
g.addArc(1, 2) 
g.addArc(2, 0)
g.addArc(2,3)
g.addArc(3,3) 
 

IsReachableBFS(g,1, 3)
g.IsReachableDFS(1, 3)