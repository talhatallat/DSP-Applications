import numpy as np
import scipy.fftpack
from scipy.signal import lfilter
import matplotlib.pyplot as plt
from scipy.io import wavfile
# ---------------------creating an input signal---------------------

plt.close("all")
fs=8000
b=np.array([1,0,0,0,0,0,0,0,0.8])
a,N=1,128
ip=np.zeros(N);
ip[0]=1; #apply impulse to input
op=lfilter(b,a,ip)
plt.plot(op)
plt.grid()
plt.figure(1)
plt.title('Impulse Response')
plt.xlabel('n') 
plt.ylabel('h(n)')
plt.show()

NFFT=1024 # No. of values in FFT
M = 2*np.abs(scipy.fftpack.fft(op,NFFT))/N
M = M[0:int(NFFT/2)] #slicing operation to avoid mirroring
freq = np.arange(0,NFFT/2) #frequency vector
freq = freq*fs/NFFT
plt.figure(2)
plt.plot(freq,M)
plt.title('Spectrum of Single Echo Filter (Delay d=8)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (V)')
plt.grid()
plt.show() 

plt.stem(op[0:11])
plt.grid()
plt.title('Impulse Response stem plot')
plt.xlabel('n') 
plt.ylabel('h(n)')
plt.show()

b=np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.8])
a,N=1,128
ip=np.zeros(N);
ip[0]=1; #apply impulse to input
op=lfilter(b,a,ip)
plt.plot(op)
plt.grid()
plt.title('Impulse Response')
plt.xlabel('n') 
plt.ylabel('h(n)')
plt.show()



NFFT=1024 # No. of values in FFT
M = 2*np.abs(scipy.fftpack.fft(op,NFFT))/N
M = M[0:int(NFFT/2)] #slicing operation to avoid mirroring
freq = np.arange(0,NFFT/2) #frequency vector
freq = freq*fs/NFFT
plt.plot(freq,M)
plt.title('Spectrum of Single Echo Filter (Delay d=8)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (V)')
plt.grid()
plt.show()


plt.stem(op[0:22])
plt.grid()
plt.title('Impulse Response stem plot')
plt.xlabel('n') 
plt.ylabel('h(n)')
plt.show()
