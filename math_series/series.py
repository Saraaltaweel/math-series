def fibonacci(n):
    
  return  sum_series(n)


def lucas(n):
    
    return  sum_series(n,2,1)

        
def sum_series(n,num1=0,num2=1):
    if n>=0:
        if n==0:
          return str(n)
        if n==1:
          return str(n)
        else:
          return str(sum_series(n-1,num1,num2) + sum_series(n-2,num1,num2))