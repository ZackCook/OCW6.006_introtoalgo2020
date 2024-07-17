'''
This is an exercise in developing the factorial algorithm, for practicing recursion and working with call stacks
'''

def iterFactorial(n):
    result = 1
    if n == 0:
        return result
    else:   
        for i in range(n,0,-1):
            result *= i
        return result
    
        
print("testing iterative")
x = iterFactorial(3)
print("3!=",x)
x = iterFactorial(0)
print("0!=",x)
x = iterFactorial(1)
print("1!=",x)
x = iterFactorial(5)
print("5!=",x)

def recursiveFactorial(n):
    if n == 0:
        return 1
    else:
        return n * recursiveFactorial(n-1)
    
print("testing recursive")
x = recursiveFactorial(3)
print("3!=",x)
x = recursiveFactorial(0)
print("0!=",x)
x = recursiveFactorial(1)
print("1!=",x)
x = recursiveFactorial(5)
print("5!=",x)
