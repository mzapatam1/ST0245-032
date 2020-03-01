from time import time
import random
def arreglo(l):
  a=[]
  h=0
  while h<l:
    a.append(random.randrange(100))
    h=h+1
  return a
def insertionSort(arr):
  for i in range (1,len(arr)):
    aux = arr[i]
    j = i-1
    while j>=0 and aux < arr[j]:
      arr[j+1]=arr[j]
      j = j-1
    arr[j+1]=aux
  return arr
for i in range (21):
  start=time()
  b=random.randrange(1000,3000,100)
  insertionSort(arreglo(b))
  final=time()-start
  print(final, b)
print ("Merge Sort")
  
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1 

for i in range (21):
  start=time()
  b=random.randrange(5000,15000,100)
  mergeSort(arreglo(b))
  final=time()-start
  print(final, b)