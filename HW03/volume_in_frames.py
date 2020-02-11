# import
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# def


def sample2frame(sample_rate, samples, frame_size, overlap):
    step = frame_size-overlap
    frames = []
    for idx in range(0, len(samples), step):
        f = samples[idx:idx+frame_size]
        if len(f) < frame_size:
            f = np.append(f, np.zeros(frame_size-len(f)))
            frames.append(f)
            break
        else:
            frames.append(f)
    frames = np.array(frames)
    frame_count, _ = frames.shape
    frame_time = np.arange(0, frame_count)*step/sample_rate
    return frame_time, frames


def frames2volume(frames):
    abs_volume = []
    log_volume = []
    for row_frame in frames:
        abs_frame = row_frame-np.median(row_frame)
        log_frame = row_frame-np.mean(row_frame)
        abs_volume.append(np.sum(np.abs(abs_frame)))
        log_volume.append(np.sum(log_frame**2))
    log_volume = np.array(10*np.log10(log_volume))
    abs_volume = np.array(abs_volume)
    return abs_volume, log_volume


if __name__ == "__main__":
    # load file
    sr, wav = wavfile.read('hello.wav')
    sample_time = np.arange(0, len(wav))/sr

    # get frames
    frame_size = 512
    overlap = 128
    frame_time, frames = sample2frame(sr, wav, frame_size, overlap)

    # calculate volume
    abs_volume, log_volume = frames2volume(frames)

    # plot
    plt.subplot(311)
    plt.ylabel('amplititude')
    plt.plot(sample_time, wav)
    plt.subplot(312)
    plt.ylabel('abs volume')
    plt.plot(frame_time, abs_volume)
    plt.subplot(313)
    plt.ylabel('log volume')
    plt.plot(frame_time, log_volume)
    plt.xlabel('time')
    plt.tight_layout()
    plt.show()
