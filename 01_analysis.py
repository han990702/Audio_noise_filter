import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import librosa

#주파수 스펙트럼 그래프 그리기
def plot_spectrum(audio, sample_rate):
    n = len(audio)#오디오의 길이
    T = 1 / sample_rate#샘플링 주기
    yf = fft(audio)#고속푸리에변환
    xf = fftfreq(n, T)[:n // 2]#샘플주파수(양수만 취함)
    plt.plot(xf, (2 / n) * np.abs(yf[:n // 2]))#그래프를 그림
    #절대값을 취하므로 2를 곱하고, n으로 나누어 정규화
    
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.show()

# librosa로 오디오 파일 불러오기
original_audio, sample_rate_original = librosa.load('test.wav', sr=None)
hum_audio, sample_rate_hum = librosa.load('humtest.wav', sr=None)
elec_audio, sample_rate_elec = librosa.load('electest.wav', sr=None)

#각 오디오 파일에 대한 그래프 보여주기
plot_spectrum(original_audio, sample_rate_original)
plot_spectrum(hum_audio, sample_rate_hum)
plot_spectrum(elec_audio, sample_rate_elec)
