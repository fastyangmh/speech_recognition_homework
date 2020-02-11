# import
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

# def


def encrypt(x):
    z = x
    z = np.where(x > 0, 1-x, -1-x)
    return z[::-1]


if __name__ == "__main__":
    # load wav
    sr, y = wavfile.read('hello.wav')
    t = np.arange(len(y))/sr

    # encrypt
    y_en = encrypt(y)

    # write
    wavfile.write('hello_encrypted.wav', sr, y_en)

    # plot
    plt.subplot(211)
    plt.title('original signal')
    plt.plot(t, y)
    plt.subplot(212)
    plt.title('encrypted signal')
    plt.plot(t, y_en)
    plt.tight_layout()
    plt.show()
