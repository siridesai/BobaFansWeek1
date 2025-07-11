from numba import njit
import numpy as np
from scipy.ndimage import generate_binary_structure, iterate_structure
from matplotlib import mlab, pyplot as plt

# need to figure out best values for n_neighbors and cutoff_percentage
n_neighbors = 2
cutoff_percentage = 0.6

def spectro(samples):
    #N = len(samples)
    sampling_rate = 44100
    #times = np.arange(N) * (1/sampling_rate)
    #ck = np.fft.rfft(samples)
   #k = np.arange(N//2 + 1)
   # amps = np.abs(ck)/N
    #amps[1:-1] *= 2
    #ak = amps
    #fk = k * sampling_rate/N

    fig, ax = plt.subplots()
    S, freqs, times2, im = ax.specgram(
    samples,
    NFFT=4096,
    Fs=sampling_rate,
    window=mlab.window_hanning,
    noverlap=4096 // 2,
    mode='magnitude',
    scale="dB"
    )
    fig.colorbar(im)
    ax.set_xlabel("Time [seconds]")
    ax.set_ylabel("Frequency (Hz)")
    ax.set_title("Spectrogram of Sample")
    ax.set_ylim(0, 4000);
    return S
    
def calculate_amp_min(S, cutoff_percentage):
    S = S.ravel()  
    ind = round(len(S) * cutoff_percentage)  
    amp_min = np.partition(S, ind)[ind] 
    return amp_min

@njit  
def _peaks(data_2d, neighborhood_row_offsets, neighborhood_col_offsets, amp_min):
    peaks = []
    for c, r in np.ndindex(*data_2d.shape[::-1]):
        if data_2d[r, c] <= amp_min:
            continue
        for dr, dc in zip(neighborhood_row_offsets, neighborhood_col_offsets):
            if dr == 0 and dc == 0:
                continue
            if not (0 <= r + dr < data_2d.shape[0]):
                continue
            if not (0 <= c + dc < data_2d.shape[1]):
                continue
            if data_2d[r, c] < data_2d[r + dr, c + dc]:
                break
        else:
            peaks.append((r, c))
    return peaks

def local_peak_locations(data_2d, amp_min):
    base_structure = generate_binary_structure(2,1)
    neighborhood = iterate_structure(base_structure, n_neighbors)
    assert neighborhood.shape[0] % 2 == 1
    assert neighborhood.shape[1] % 2 == 1
    nbrhd_row_indices, nbrhd_col_indices = np.where(neighborhood)
    neighborhood_row_offsets = neighborhood_row_indices - neighborhood.shape[0] // 2
    neighborhood_col_offsets = neighborhood_col_indices - neighborhood.shape[1] // 2
    return _peaks(data_2d, neighborhood_row_offsets, neighborhood_col_offsets, amp_min=amp_min)

def return_peaks(samples):
    S = spectro(samples)
    amp_min = calculate_amp_min(S, cutoff_percentage)
    peaks = local_peak_locations(S, amp_min)
    return peaks