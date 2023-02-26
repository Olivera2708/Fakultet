import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

def nnInter(input, factor):
    width, height = input.shape

    new_width = int(width * factor)
    new_height = int(height * factor)

    out = np.zeros((new_width, new_height))
    for x in range(new_width):
        for y in range(new_height):
            out[x, y] = input[int(x/factor), int(y/factor)]

    return out

def scaleNN(input, factor):
    # rastavljanje 3D matrice na 3 x 2D matrice (po RGB kanalima)
    R = input[:,:,0]
    G = input[:, :, 1]
    B = input[:, :, 2]

    # skaliranje
    R = nnInter(R, factor)
    G = nnInter(G, factor)
    B = nnInter(B, factor)

    # spajamo 3 x WxH matrice i konvertujemo float 0..1 u uint
    return (np.dstack((R,G,B)) * 255.999).astype(np.uint8)



def bilinearInter(input, factor):
    width, height = input.shape

    new_width = int(width * factor)
    new_height = int(height * factor)

    out = np.zeros((new_width, new_height))

    blockX = np.linspace(0, new_width - 1, width)
    blockY = np.linspace(0, new_height - 1, height)

    blocksX = width - 1
    blocksY = height - 1

    for itBlockX in range(blocksX):
        for itBlockY in range(blocksY):
            in11 = input[itBlockY, itBlockX]
            in12 = input[itBlockY, itBlockX + 1]
            in21 = input[itBlockY + 1, itBlockX]
            in22 = input[itBlockY + 1, itBlockX + 1]

            x1 = int(blockX[itBlockX])
            x2 = int(blockX[itBlockX + 1])
            y1 = int(blockY[itBlockY])
            y2 = int(blockY[itBlockY + 1])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    out1 = ((x2 - x) / (x2 - x1)) * in11 + ((x - x1) / (x2 - x1)) * in12
                    out2 = ((x2 - x) / (x2 - x1)) * in21 + ((x - x1) / (x2 - x1)) * in22
                    out[y, x] = ((y2 - y) / (y2 - y1)) * out1 + ((y - y1) / (y2 - y1)) * out2
    return out

def scaleBilinear(input, factor):
    # rastavljanje 3D matrice na 3 x 2D matrice (po RGB kanalima)
    R = input[:, :, 0]
    G = input[:, :, 1]
    B = input[:, :, 2]

    # skaliranje
    R = bilinearInter(R, factor)
    G = bilinearInter(G, factor)
    B = bilinearInter(B, factor)

    # spajamo 3 x WxH matrice i konvertujemo float 0..1 u uint
    return (np.dstack((R, G, B)) * 255.999).astype(np.uint8)


if __name__ == '__main__':
    # c)
    A = np.array([[1,2],
                  [3,4]])
    print(nnInter(A, 3))

    # e)
    image = img.imread('./Lenna.png')
    nnScaled = scaleNN(image, 3)
    img.imsave('Lenna NN.png', nnScaled)

    plt.imshow(nnScaled)

    # h)
    A = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
    print(bilinearInter(A, 3))

    # j)
    bilinearScaled = scaleBilinear(image, 3)
    img.imsave('Lenna (bilinear).png', bilinearScaled)
    plt.imshow(bilinearScaled)
    plt.show()

