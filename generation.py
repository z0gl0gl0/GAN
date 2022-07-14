#!/usr/bin/env python

from keras.models import load_model
import matplotlib.pyplot as plt
import sys
import asyncio
import numpy as np
from PIL import Image

def main():
    dataset = sys.argv[1]
    n_epochs = sys.argv[2]
    generator = load_model(f"generator_model_{dataset}_{n_epochs}.h5")
    discriminator = load_model(f"discriminator_model_{dataset}_{n_epochs}.h5")
    noise = np.random.normal(0, 1, (1, 100))
    eps = 1e-5
    k = 0
    maxi = int(sys.argv[3])
    n_dix = maxi // 10 + 1
    while k < maxi:
        noise = np.random.normal(0, 1, (1, 100))
        img = generator.predict(noise)
        test = discriminator.predict(img)[0, 0]
        #if test <= eps:
        k += 1
        img = 0.5*img + 0.5
        plt.imshow(img[0, :, :, :])
        plt.title(f"validity : {test:06}")
        plt.axis('off')
        plt.savefig(f"resultats/result_{dataset}_{k:0{n_dix}}.png")
        plt.close()
    
main()
