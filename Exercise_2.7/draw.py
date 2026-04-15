import matplotlib.pyplot as plt
from scipy.io import loadmat
import numpy as np

# Load the .mat file
def load_mat(filename):
    data = loadmat(filename)
    label = list(data.keys())[-1]
    array = np.array(data[label])[0]
    return 10*np.log10(array)


withCP_files = ['MSE_ls_4QAM.mat',
                'MSE_mmse_4QAM.mat',
                'MSE_dnn_4QAM.mat'
                ]

withoutCP_files = ['MSE_ls_4QAM_CP_FREE.mat',
                'MSE_mmse_4QAM_CP_FREE.mat',
                'MSE_dnn_4QAM_CP_FREE.mat'
                ]

SNRs = [5, 10, 15, 20, 25, 30, 35, 40]
plt.plot(SNRs, load_mat(withCP_files[0]), marker='o', linestyle='-', color='r', label='LS')
plt.plot(SNRs, load_mat(withCP_files[1]), marker='s', linestyle='-.', color='r', label='MMSE')
plt.plot(SNRs, load_mat(withCP_files[2]), marker='^', linestyle='--', color='r', label='DNN')

plt.plot(SNRs, load_mat(withoutCP_files[0]), marker='o', linestyle='-', color='k', label='LS w/o CP')
plt.plot(SNRs, load_mat(withoutCP_files[1]), marker='s', linestyle='-.', color='k', label='MMSE w/o CP')
plt.plot(SNRs, load_mat(withoutCP_files[2]), marker='^', linestyle='--', color='k', label='DNN w/o CP')

plt.xlabel('SNR (dB)')
plt.ylabel('MSE (dB)')
plt.legend()
plt.show()
