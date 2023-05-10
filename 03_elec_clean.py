import librosa
import numpy as np
import scipy.signal
import soundfile as sf

def lowpass_filter(audio_data, sample_rate, cutoff_freq, order):
    b, a = scipy.signal.butter(order, cutoff_freq, btype='low', fs=sample_rate)#low pass filter 설계
    filtered_audio = scipy.signal.lfilter(b, a, audio_data)#filter 적용
    return filtered_audio

# 오디오 파일 불러오기
audio_data, sample_rate = librosa.load('electest.wav', sr=None)

# Cut-off frequency
cutoff_freq = 2000
# Filter order
order = 2#높을수록 주파수 영역을 더 정확하게 컨트롤 할 수 있음

# low pass filter 적용
filtered_audio_data = lowpass_filter(audio_data, sample_rate, cutoff_freq, order)

#필터링된 오디오 파일 저장
sf.write('electest_clean.wav', filtered_audio_data, sample_rate)
