import time

def suma(n):
    if n == 1:
        return 1
    return n + suma(n-1)

start_time = time.time()
print(f"{suma(3)} -> {(time.time() - start_time):.20f}")
