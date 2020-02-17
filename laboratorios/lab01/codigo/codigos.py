
def punto1(n):
    if (n<=2):
        return n
    else:
        return punto1(n-1)+punto1(n-2)
print (punto1(4))
