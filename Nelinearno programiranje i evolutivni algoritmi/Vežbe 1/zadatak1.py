def fibonaciFor(n):
    prvi = 1
    drugi = 1
    for i in range(n-2):
        sledeci = prvi + drugi
        prvi = drugi
        drugi = sledeci

    return drugi

def fibonaciWhile(n):
    prvi = 1
    drugi = 1
    i = n - 2
    
    while i > 0:
        i -= 1
        sledeci = prvi + drugi
        prvi = drugi
        drugi = sledeci

    return drugi

print(fibonaciFor(10))
print(fibonaciWhile(10))