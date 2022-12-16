import matplotlib.pyplot as plt
import numpy as np

#%%
"""两个窗函数的参数分别为0.46和0.5"""
def Windows(width,parameter):
    function=np.zeros(width)
    for n in range(width):
        function[n]=(1-parameter)-parameter*np.cos((2*3.14*n)/(width-1))
    return function
hamming=Windows(512,0.46)
hanning=Windows(512,0.5)
plt.figure(0)
plt.plot(hanning)
plt.show()
# plt.savefig("hanning.png",dpi=1000)
plt.figure(1)
plt.plot(hamming)
plt.show()
# plt.savefig("hamming.png",dpi=1000)

#%%
"""分帧"""
def framing(audio_1,N,move):#N代表帧长，move代表帧移
    framing=np.zeros(1)
    for i in range(0,len(audio_1),move):
        Calculation=np.zeros(N)
        print(len(audio_1[i:i+N]))
        if len(audio_1[i:i+N])==N:
            Calculation=audio_1[i:i+N]*hamming
            framing=np.append(framing,Calculation)
        else:
            Calculation=audio_1[i:i+N]*hamming[0:len(audio_1[i:i+N])]
            framing=np.append(framing,Calculation)
    return framing
x=framing(audio_1,512,256)  #audio_1:音频
plt.plot(x)
plt.savefig("分帧.png",dpi=1000)

#%%
"""短时能量分析"""
def short_power_function_1(audio_1, N, choose):
    short_power = np.zeros(1)
    if choose == 1:
        for i in range(0, len(audio_1), 256):
            Calculation_1 = np.zeros(N)
            print(len(audio_1[i:i + N]))
            if len(audio_1[i:i + N]) == N:
                Calculation_1 = audio_1[i:i + N] * hamming
                Calculation_1 = Calculation_1 * Calculation_1
                short_power = np.append(short_power, Calculation_1)
            else:
                Calculation_1 = audio_1[i:i + N] * hamming[0:len(audio_1[i:i + N])]
                Calculation_1 = Calculation_1 * Calculation_1
                short_power = np.append(short_power, Calculation_1)
    else:
        for i in range(0, len(audio_1), 256):
            Calculation_1 = np.zeros(N)
            print(len(audio_1[i:i + N]))
            if len(audio_1[i:i + N]) == N:
                Calculation_1 = np.abs(audio_1[i:i + N]) * hamming
                short_power = np.append(short_power, Calculation_1)
            else:
                Calculation_1 = np.abs(audio_1[i:i + N]) * hamming[0:len(audio_1[i:i + N])]
                short_power = np.append(short_power, Calculation_1)
    return short_power

x1 = short_power_function_1(audio_1, 512, 1)
x2 = short_power_function_1(audio_1, 512, 0)
plt.figure(0)
plt.plot(x1)
plt.savefig("能量1.png", dpi=1000)
plt.figure(1)
plt.plot(x2)
plt.savefig("能量2.png", dpi=1000)

#%%
"""过零率"""
def zeros_count(audio_1, N, T):  #T代表门限

    def sgn(a, T):
        #定义一个判别函数，对输入数据a,大于T的定义为1，小于T的定义为-1
        if a >= T:
            return 1
        else:
            return -1
    count = np.zeros(1)
    for i in range(0, len(audio_1), 256):
        Calculation = 0
        if len(audio_1[i:i + N]) == N:
            for j in range(N):
                Calculation_1 = 0.5 * (np.abs(sgn(audio_1[i + j], T) - sgn(audio_1[i + j - 1], T)))
                #            print(Calculation_1)
                Calculation = Calculation + Calculation_1
            count = np.append(count, Calculation)
        else:
            for j in range(len(audio_1[i:i + N])):
                Calculation_1 = 0.5 * (np.abs(sgn(audio_1[i + j], T) - sgn(audio_1[i + j - 1], T)))
                Calculation = Calculation + Calculation_1
            count = np.append(count, Calculation)
    return count

