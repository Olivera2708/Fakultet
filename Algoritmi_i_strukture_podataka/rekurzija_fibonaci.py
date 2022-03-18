import time

def fib_binarni(n):
    if n == 1 or n == 2:
        return 1
    return fib_binarni(n-1) + fib_binarni(n-2)
    
start1 = time.time()
print(f"{fib_binarni(10)} -> {(time.time()-start1):.20f}")