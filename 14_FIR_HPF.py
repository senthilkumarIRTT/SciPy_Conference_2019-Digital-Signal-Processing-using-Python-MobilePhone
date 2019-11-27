#FIR HPF filter Design using Windowing techniques
#comparing own function with built-in function

from numpy import cos, sin, pi, absolute, arange, zeros
from scipy.signal import hamming,firwin, freqz
import matplotlib.pyplot as plt
#from pylab import figure, clf, plot, xlabel, ylabel, xlim, ylim, title, grid, axes, show

#N = eval(input('Enter the filter order N='))
N=7

#fc = eval(input('Enter the cutoff frequency='))
fc= 500

#Fs = eval(input('Enter the sampling frequency='))
Fs =2000
FN = 2*fc    #Nyquist rate

# Use firwin with a Hamming window to create a lowpass FIR filter.
taps = firwin(N, fc/Fs, pass_zero=False,window=('hamming'))

print('FIR Low Pass Filter Coefficients h[n]=',taps)

#Hamming window generation
wn = hamming(N)
print('Normalized digital cut-off frequency',fc/Fs)
wc = (fc/Fs)*pi
print('Digital cut-off frequency',wc)
K = 1.414  #gain

#FIR filter cofficients generated from formula directly
Tuo = (N-1)/2
hd  = zeros(N)
h   = zeros(N)
for n in range(N):
    if n==Tuo:
        hd[n] = 1-(wc/pi)
        
    else:
        hd[n] = (sin(pi*(n-Tuo))-sin(wc*(n-Tuo)))/(pi*(n-Tuo))
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
plt.plot((W/max(W)), absolute(H), linewidth=2)
#plot((W/max(W))*Fs,absolute(H), linewidth=2)
#xlabel('Frequency in Hz------->')
plt.xlabel('Normalized Digital Frequency (Wc/pi)--->')
plt.ylabel('Gain')
plt.title('Frequency Response of High Pass FIR Filter using Built-in Function')
plt.ylim(-0.05, 1.05)
plt.grid(True)

del W
del H
#------------------------------------------------------------------
# Plot the magnitude response of the filter using own function
#------------------------------------------------------------------

plt.figure(3)

W,H = freqz(h, worN=8000)
plt.plot((W/max(W)),absolute(H), linewidth=2)
#plot((W/max(W))*Fs,absolute(H), linewidth=2)
#xlabel('Frequency in Hz------->')
plt.xlabel('Normalized Digital Frequency (Wc/pi)------->')
plt.ylabel('Gain')
plt.title('Frequency Response of High Pass FIR Filter using Own Formula based')
plt.ylim(-0.05,1.05)
plt.grid(True)
plt.show()

#Result
##Enter the filter order N=7
##Enter the cutoff frequency= 500
##Enter the sampling frequency= 2000
##FIR Low Pass Filter Coefficients h[n]= [-0.00594298 -0.04885196 -0.17160345  0.74261107 -0.17160345 -0.04885196
## -0.00594298]
##Normalized digital cut-off frequency 0.25
##Digital cut-off frequency 0.7853981633974483
##FIR Low Pass Filter coefficients using formula h[n]= [-0.00600211 -0.04933803 -0.17331089  0.75       -0.17331089 -0.04933803
## -0.00600211]
