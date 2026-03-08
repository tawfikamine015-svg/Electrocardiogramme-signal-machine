import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
 # signal de l'éléctrocardiogramme 10s
fs = 1000
t = np.linspace(0, 10, 10 * fs)
ecg = signal.gausspulse(t - 1, fc=2) + signal.gausspulse(t - 2, fc=2)
bruit = np.random.normal(0, 0.5, len(t))
brut_ecg = ecg + bruit
# filtre pass-bas 5hz
b, a = signal.butter(6, 0.02)
filtre_ecg = signal.filtfilt(b, a, brut_ecg)
# visuel
plt.figure(figsize=(10, 4))
plt.plot(t[:2000], brut_ecg[:2000], label='Signal brut', alpha=0.5)
plt.plot(t[:2000], filtre_ecg[:2000], label='Signal filtré', color='red')
plt.title("processeur de signal brut")
plt.legend()
plt.show()

# Utilisation d'un filtre pass-bas après avoir simulé du bruit artificiel/réel

# Les pics du signal filtré peuvent indiquer un battement du coeur
peaks, _ = signal.find_peaks(filtre_ecg, distance=fs/2)

# BPM
bpm = len(peaks) * 6

print(f"--- résultats d'analyse ---")
print(f"BPM: {bpm} BPM")
print(f"Statut: {'Normal' if 60 <= bpm <= 100 else 'Danger'}")

