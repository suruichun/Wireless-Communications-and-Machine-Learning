# Exercise 3.1: Learning-based Signal Detection for OFDM Systems

This repository provides the starter code for Exercise 3.1. Your task is to use Deep Learning (FC-DNN) to implicitly estimate the channel and recover transmitted bits in an OFDM system, based on the paper by Ye et al. [15]. You will modify network dimensions, modulation schemes, and pilot configurations to evaluate the system's Bit Error Rate (BER).

The results are recorded in ./DNN_Detection/results.csv

## What You Need to Do
1. Obtain H_dataset from https://github.com/haoyye/OFDM_DNN
2. Unzip the dataset: $ cat H_dataset.zip*>H_dataset.zip $ unzip H_dataset.zip
3. Go to folder ./DNN_Detection
4. Open Main.py and check 'hiddendims = np.array([500, 250, 120], int)'
5. Run train_hw3b.bat for part (b).
6. Run train_hw3c.bat for part (c).
7. Run train_hw3d.bat for part (d).
8. Open Main.py and modify 'hiddendims = np.array([500, 250, 120], int)' to 'hiddendims = np.array([1600, 900, 500], int)'
9. Run python3 Main.py --Pilots 64 --SNR 5 --r1 0 --r2 128 for part (d).
10. Open Main.py and modify 'IS_Training = True' to 'IS_Training = False'.
11. Do 3.~8. for evaluation.

