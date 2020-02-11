# import
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

# def


def readwav(filepath):
    sr, wav = wavfile.read(filepath)
    t = np.arange(0, len(wav))/sr
    return sr, t, wav


if __name__ == "__main__":
    # load wav
    h = readwav('h.wav')
    i = readwav('i.wav')
    d = readwav('d.wav')
    hide = readwav('hide.wav')

    # plot
    plt.subplot(411)
    plt.title('/h/')
    plt.plot(h[1], h[2])
    plt.ylabel('Amplititude')
    plt.subplot(412)
    plt.title('/i/')
    plt.plot(i[1], i[2])
    plt.ylabel('Amplititude')
    plt.subplot(413)
    plt.title('/d/')
    plt.plot(d[1], d[2])
    plt.ylabel('Amplititude')
    plt.subplot(414)
    plt.title('/hide/')
    plt.plot(hide[1], hide[2])
    plt.ylabel('Amplititude')
    plt.xlabel('Time')
    plt.tight_layout()
    plt.show()
