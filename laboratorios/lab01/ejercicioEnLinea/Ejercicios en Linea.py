def factorial(n):
     if(n>0):
      return n* factorial(n-1) 
     else:
      return 1
def bunnyears(bunnies):
    if(bunnies==0):
     return 0
    else:
        return 2+bunnyears(bunnies-1)
def fibonacci(n):
    if(n<2):
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)
def bunnyears2(bunnies):
    if(bunnies==0):
        return 0
    if(bunnies%2==1):
        return 2+bunnyears2(bunnies-1)
    else:
        return 3+bunnyears(bunnies-1)
def triangle(rows):
    if(rows<2):
        return rows
    else:
     return rows + triangle(rows-1)
def groupsum6(start,nums,target):
    if(start==len(nums)):
        if(target==0):
            return True
        else:
            return False
    elif (nums[start]==6):
        return groupsum6(start+1,nums,target-nums[start])
    elif(groupsum6(start+1,nums,target-nums[start])):
        return True
    else:
        return groupsum6(start+1,nums,target)
    
      
        
    
 
    

