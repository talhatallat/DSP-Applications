import numpy as np
import scipy.fftpack
from scipy.signal import lfilter
import matplotlib.pyplot as plt
from scipy.io import wavfile
plt.close("all")
fs, audio = wavfile.read('c:\Temp\speech_dft.wav') # Applying a real audio signal to the input and observing the results.
b=np.zeros(int(fs/2)+1) # Adds a 0.5 sec delay
audio=np.append(audio,b) # Adding zeros prevents the end of the file being truncated.
NN=len(audio)*1.0
t=np.arange(0,NN)/fs
plt.plot(t,audio)
plt.title ('Input Audio');
plt.grid()
plt.show()
b[0]=1
b[int(fs/2)]=0.8
a=1
audioOP=lfilter(b,a,audio)
plt.plot(t,audioOP)
plt.title ('Output Audio');
plt.grid()
plt.show()
diff=audio-audioOP
plt.plot(t,diff)
plt.title ('Input Audio-Output Audio');
plt.grid()
plt.show()
wavfile.write('c:\Temp\save_speech_dft.wav',fs,audio)
audioOP = np.asarray(audioOP, dtype=np.int16)
wavfile.write('c:\Temp\echo_speech_dft.wav',fs,audioOP)

N=6; R=int(fs/2)+1; alpha=0.8;
b=np.zeros(N*R+1);
b[N*R]=-alpha**N; b[0]=1;
a=np.zeros(R+1);
a[R]=-alpha; a[0]=1;
audioOP=lfilter(b,a,audio)
plt.plot(t,audioOP)
plt.title ('Output Audio (Multiple Echo)');
audioOP = np.asarray(audioOP, dtype=np.int16)
wavfile.write('c:\Temp\mult_echo_speech_dft.wav',fs,audioOP)
