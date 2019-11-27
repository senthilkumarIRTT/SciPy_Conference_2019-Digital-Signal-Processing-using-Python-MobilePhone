#FIR BPF filter Design using Windowing techniques
#comparing own function with built-in function

from numpy import cos, sin, pi, absolute, arange, zeros
from scipy.signal import hamming,firwin, freqz
#from pylab import figure, clf, plot, xlabel, ylabel, xlim, ylim, title, grid, axes, show
import matplotlib.pyplot as plt

#N = eval(input('Enter the filter order N='))
N = 31
#[fc1,fc2] = eval(input('Enter the cutoff frequency='))
[fc1,fc2]=[300,600]
#Fs = eval(input('Enter the sampling frequency='))
Fs = 2000
FN = 2*fc2    #Nyquist rate

# Use firwin with a Hamming window to create a lowpass FIR filter.
taps = firwin(N, [fc1/Fs,fc2/Fs],pass_zero=False, window=('hamming'))

print('FIR Band Pass Filter Coefficients h[n]=',taps)

 #Hamming window generation
wn = hamming(N)
print('Normalized digital cut-off frequencies',fc1/Fs,fc2/Fs)
wc1 = (fc1/Fs)*pi
wc2 = (fc2/Fs)*pi
print('Digital cut-off frequencies',wc1,wc2)
K = 0.8  #gain
#FIR filter cofficients generated from formula directly
Tuo = (N-1)/2
hd  = zeros(N)
h   = zeros(N)
for n in range(N):
    if n==Tuo:
        hd[n] = (wc2-wc1)/pi
        
    else:
        hd[n] = (sin(wc2*(n-Tuo))-sin(wc1*(n-Tuo)))/(pi*(n-Tuo))
    h[n] = hd[n]*wn[n]
    h[n] = h[n]
print('FIR Low Pass Filter coefficients using formula h[n]=',h)


  

#------------------------------------------------
# Plot the FIR filter coefficients.
#------------------------------------------------

plt.figure(1)
plt.plot(taps, 'bo-', linewidth=2)
plt.xlabel('Filter taps--------->')
plt.ylabel('Filter coefficients-------->')
plt.title('Filter Coefficients')
plt.grid(True)

#------------------------------------------------------------------
# Plot the magnitude response of the filter using Built-in function
#------------------------------------------------------------------

plt.figure(2)


W,H = freqz(taps, worN=8000)
#plot((W/max(W)), absolute(H), linewidth=2)
plt.plot((W/max(W))*Fs,absolute(H), linewidth=2)
plt.xlabel('Frequency in Hz------->')
#xlabel('Normalized Digital Frequency (Wc/pi)--->')
plt.ylabel('Gain')
plt.title('Frequency Response of Band Pass FIR Filter using Built-in Function')
plt.ylim(-0.05, 1.05)
plt.grid(True)

del W
del H
#------------------------------------------------------------------
# Plot the magnitude response of the filter using own function
#------------------------------------------------------------------

plt.figure(3)

W,H = freqz(h, worN=8000)
#plot((W/max(W)),absolute(H), linewidth=2)
plt.plot((W/max(W))*Fs,absolute(H), linewidth=2)
plt.xlabel('Frequency in Hz------->')
#xlabel('Normalized Digital Frequency (Wc/pi)------->')
plt.ylabel('Gain')
plt.title('Frequency Response of Band Pass FIR Filter using Own Formula based')
plt.ylim(-0.05,1.05)
plt.grid(True)
plt.show()

#Result
##Enter the filter order N= 31
##Enter the cutoff frequency= [300,600]
##Enter the sampling frequency= 2000
##Normalized digital cut-off frequencies 0.15 0.3
##Digital cut-off frequencies 0.47123889803846897 0.9424777960769379
