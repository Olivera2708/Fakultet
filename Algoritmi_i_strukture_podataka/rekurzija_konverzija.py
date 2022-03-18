import time

def konverzija(n, osnova):
    if n == 0:
        return ""
    else:
        broj = n % osnova
        if broj > 9:
            return konverzija(n // osnova, osnova) + chr(55+broj)
        else:
            return konverzija(n // osnova, osnova) + str(broj)


start = time.time()
print(f"{konverzija(1487639,16)} -> {(time.time() - start):.20f}")
