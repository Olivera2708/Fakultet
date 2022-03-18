import time

def max (maximum, niz):
    if niz == []:
        return maximum
    if maximum < niz[0]:
        return max(niz[0], niz[1:])
    else:
        return max(maximum, niz[1:])

start_time = time.perf_counter()
niz = [1,5,7,3,6,12,3,5]
maxi = max(niz[0], niz)
print(f"{maxi} -> {(time.perf_counter() - start_time):.20f}")