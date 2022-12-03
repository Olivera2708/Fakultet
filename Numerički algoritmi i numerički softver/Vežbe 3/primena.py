import numpy as np
from gs import gauss_seidel

def makeH(C):
    _, cols = C.shape

    H = np.zeros(C.shape)
    for col in range(cols):
        H[:, col] = C[:, col]/np.sum(C[:, col])
    
    return H

def sortPages(pages, r):
    
    ranked_pages = list(zip(pages, r))

    return sorted(ranked_pages, key=lambda x: x[1], reverse=True)


C = np.array([
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
])

H = makeH(C)

rows, _ = H.shape

d = 0.85
p = np.ones(rows)*((1-d)/rows)
I = np.eye(rows)

r0 = np.zeros(rows)
r = gauss_seidel(I - d*H, p, r0)

np.set_printoptions(precision=4)
print(r)

pages = [
    'page 1',
    'page 2',
    'page 3',
    'page 4',
    'page 5',
    'page 6',
    'page 7',
    'page 8',
    'page 9',
    'page 10'
]



sortedPages = sortPages(pages, r)

print([page_rank[0] for page_rank in sortedPages])