import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('results.csv')
print(df)
dfmu2 = df[df['mu']==2]
dfmu2_partb = dfmu2[dfmu2['r1']==16]

SNR = [5, 10, 15, 20, 25]
NumP = [8, 16, 64]
BERb = np.zeros((len(NumP), len(SNR)))
for i, nump in enumerate(NumP):
    temp = dfmu2_partb[dfmu2_partb['Num_P']==nump]
    #print(temp)
    for j, snr in enumerate(SNR):
        #print(temp[temp['SNR']==snr]['BER'].values[0])
        BERb[i, j] = temp[temp['SNR']==snr]['BER'].values[0]
#print(BERb)
BERb = 10*np.log10(BERb)
plt.plot(SNR, BERb[2], marker='o', label='64 Pilots Deep Learning on QPSK')
plt.plot(SNR, BERb[1], marker='v', label='16 Pilots Deep Learning on QPSK')
plt.plot(SNR, BERb[0], marker='s', label='8 Pilots Deep Learning on QPSK')
plt.legend()
plt.grid()
plt.xlabel('SNR (dB)')
plt.ylabel('BER (dB)')
plt.title('Comparisons on QPSK')
plt.ylim(-30, -3)
plt.show()



dfmu6 = df[df['mu']==6]
dfmu6_partb = dfmu6[dfmu6['r1']==48]
SNR = [5, 10, 15, 20, 25]
NumP = [8, 16, 64]
BERc = np.zeros((len(NumP), len(SNR)))
for i, nump in enumerate(NumP):
    temp = dfmu6_partb[dfmu6_partb['Num_P']==nump]
    #print(temp)
    for j, snr in enumerate(SNR):
        #print(temp[temp['SNR']==snr]['BER'].values[0])
        BERc[i, j] = temp[temp['SNR']==snr]['BER'].values[0]
#print(BERb)
BERc = 10*np.log10(BERc)
plt.plot(SNR, BERc[2], marker='o', linestyle='--', label='64 Pilots Deep Learning on 64QAM')
plt.plot(SNR, BERc[1], marker='v', linestyle='--', label='16 Pilots Deep Learning on 64QAM')
plt.plot(SNR, BERc[0], marker='s', linestyle='--', label='8 Pilots Deep Learning on 64QAM')
plt.legend()
plt.grid()
plt.xlabel('SNR (dB)')
plt.ylabel('BER (dB)')
plt.title('Comparisons on 64QAM')
plt.ylim(-30, -3)
plt.show()

df6425 = df[(df['Num_P'] == 64) & (df['mu'] == 2) & (df['SNR'] == 5)]
print(df6425)
smallDNN = 0
for i in range(8):
    smallDNN += df6425[(df6425['r1']==16*i) & (df6425['r2']==16*i+15)]['BER'].values[0]
smallDNN = smallDNN/8
largeDNN = df6425[(df6425['r1']==0) & (df6425['r2']==127)]['BER'].values[0]
print('BER of 8 identical small DNNs: ', smallDNN)
print('BER of a large DNN: ', largeDNN)
