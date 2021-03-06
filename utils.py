import numpy as np

def merge(images, size):
    h, w = images.shape[1], images.shape[2]
    img = np.zeros((h * size[0], w * size[1]))

    for idx, image in enumerate(images):
        i = idx % size[1]
        j = int(idx / size[1])
        s0, e0, s1, e1 = j*h, j*h+h, i*w, i*w+w

        img[s0:e0, s1:e1] = image

    return img
