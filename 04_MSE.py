import librosa
import numpy as np

original_audio, sample_rate_original = librosa.load('test.wav', sr=None)
hum_clean_audio, sample_rate_hum = librosa.load('humtest_clean.wav', sr=None)
elec_clean_audio, sample_rate_elec = librosa.load('electest_clean.wav', sr=None)

MSE_hum = np.mean((original_audio - hum_clean_audio) ** 2)
MSE_elec = np.mean((original_audio - elec_clean_audio) ** 2)

print("Mean Square Error between humtest_clean and test: ", MSE_hum)
print("Mean Square Error between electest_clean and test: ", MSE_elec)
