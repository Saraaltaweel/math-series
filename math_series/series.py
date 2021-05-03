def fibonacci(n):
    
    if n==0:
        return n
    if n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    
    if n==0:
        return n
    if n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
 