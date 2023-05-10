import numpy as np
import scipy.signal
import librosa
import soundfile as sf

def notch_filter(audio_data, sample_rate, freq, quality_factor):
    b, a = scipy.signal.iirnotch(freq, quality_factor, sample_rate)#notch filter 설계
    filtered_audio = scipy.signal.lfilter(b, a, audio_data)#notch filter 적용
    return filtered_audio

# 오디오 파일 불러오기
audio_data, sample_rate = librosa.load('humtest.wav', sr=None)

# notch filter로 제거할 주파수(400Hz)
noise_freq = 400
#quality_factor값이 클 수록 더 정확히 노이즈만 제거(너무 크면 노이즈가 제거되지 않음)
quality_factor = 100  

#notch filter 적용
filtered_audio_data = notch_filter(audio_data, sample_rate, noise_freq, quality_factor)


#소리를 키우기 위한 스케일링 계수
scale = 2.0
amplified_audio_data = filtered_audio_data * scale

#clipping(허용 범위 벗어나지 못하게)
amplified_audio_data = np.clip(amplified_audio_data, np.iinfo(np.int16).min, np.iinfo(np.int16).max)


#필터를 적용해도 처음 0.06초의 비프음은 제거되지 않음(400Hz가 아니기 때문인듯)
starting_beep = 0.06  # 0.06초
for i in range(0, int(starting_beep * sample_rate)):
    amplified_audio_data[i] = 0  # 0.06초 이전의 소리 제거

# 필터링된 오디오 파일 저장
sf.write('humtest_clean.wav', amplified_audio_data, sample_rate)
