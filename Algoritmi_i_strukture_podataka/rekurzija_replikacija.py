import time

def replikacija(broj, puta):
    if puta == 1:
        return [broj]
    return [broj] + replikacija(broj, puta-1)

start = time.time()
print(f"{replikacija(5,6)} -> {(time.time()-start):.20f}")
