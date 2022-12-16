import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
def Windows(width,parameter):
    function=np.zeros(width)
    for n in range(width):
        function[n]=(1-parameter)-parameter*np.cos((2*3.14*n)/(width-1))
    return function
hamming=Windows(512,0.46)

#%%
"""短时傅里叶变换"""
def short_time_FFT(audio_1,N,move):#N代表帧长，move代表帧移
    short_time=np.zeros(1)

    for i in range(0,len(audio_1),move):
        Calculation=np.zeros(N)
        if len(audio_1[i:i+N])==N:
            Calculation=fft(audio_1[i:i+N]*hamming)#每一帧中进行傅里叶变换·
            short_time=np.append(short_time,Calculation)
        else:
            Calculation=fft(audio_1[i:i+N]*hamming[0:len(audio_1[i:i+N])])
            short_time=np.append(short_time,Calculation)
    return short_time

#%%
"""功率谱"""
def power_FFT(audio_1,N,move):##################N代表帧长，move代表帧移
    power=np.zeros(1)

    for i in range(0,len(audio_1),move):
        Calculation=np.zeros(N)
#        print(len(audio_1[i:i+N]))
        if len(audio_1[i:i+N])==N:
            Calculation=fft(audio_1[i:i+N]*hamming)*fft(audio_1[i:i+N]*hamming)
            power=np.append(power,Calculation)
        else:
            Calculation=fft(audio_1[i:i+N]*hamming[0:len(audio_1[i:i+N])])*fft(audio_1[i:i+N]*hamming[0:len(audio_1[i:i+N])])
            power=np.append(power,Calculation)
    return power

#%%
"""对数功率谱"""
def ln_power_FFT(audio_1,N,move):##################N代表帧长，move代表帧移
    power=np.zeros(1)

    for i in range(0,len(audio_1),move):
        Calculation=np.zeros(N)
#        print(len(audio_1[i:i+N]))
        if len(audio_1[i:i+N])==N:
            Calculation=np.log10(fft(audio_1[i:i+N]*hamming)*fft(audio_1[i:i+N]*hamming))
            power=np.append(power,Calculation)
        else:
            Calculation=np.log10(fft(audio_1[i:i+N]*hamming[0:len(audio_1[i:i+N])])*fft(audio_1[i:i+N]*hamming[0:len(audio_1[i:i+N])]))
            power=np.append(power,Calculation)
    return power

#%%
"""C(n)倒谱"""
def C_ln_power_FFT(audio_1,N,move):##################N代表帧长，move代表帧移
    power=np.zeros(1)

    for i in range(0,len(audio_1),move):
        Calculation=np.zeros(N)
#        print(len(audio_1[i:i+N]))
        if len(audio_1[i:i+N])==N:
            Calculation=np.log10(fft(audio_1[i:i+N]*hamming)*fft(audio_1[i:i+N]*hamming))
            Calculation=fft(Calculation)
            power=np.append(power,Calculation)
        else:
            Calculation=np.log10(fft(audio_1[i:i+N]*hamming[0:len(audio_1[i:i+N])])*fft(audio_1[i:i+N]*hamming[0:len(audio_1[i:i+N])]))
            Calculation=fft(Calculation)
            power=np.append(power,Calculation)
    return power
