def Factorial(x):
    if x==0:
        return 1
    else:
        res=x
        i=1
        while(i<x):
            res=res*i
            i=i+1
        return res
    
#func call
output=Factorial(6)   
print(output)
