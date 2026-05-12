import os
from Train import train
from Train import test
import numpy as np
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--Pilots", type=int, default=8)
    parser.add_argument("--SNR", type=float, default=20)
    parser.add_argument("--mu", type=int, default=2)
    parser.add_argument("--r1", type=int, default=-1)
    parser.add_argument("--r2", type=int, default=-1)
   
    return parser.parse_args()



class sysconfig(object):
    K = 64
    CP = K//4
    mu = 2
    Pilots = 8        # number of pilots
    with_CP_flag = True 
    SNR = 20
    Clipping = False
    Train_set_path = '../H_dataset/'
    Test_set_path = '../H_dataset/'
    Model_path = '../Models/'
    pred_range = np.arange(16,32)
    hiddendims = np.array([500, 250, 120], int)#np.array([1600, 900, 500], int)
    training_epochs = 120
    batch_size = 256
    total_batch = 256
    model_saving_step = 10
    learning_rate = 0.001
    learning_rate_decrease_step = 20     
    

def main():
    args = get_args()
    config = sysconfig()
    config.SNR = args.SNR
    config.Pilots = args.Pilots
    config.mu = args.mu
    if args.r1==-1 or args.r2==-1:
        config.pred_range = np.arange(int(8*args.mu), int(16*args.mu))
    else:
        config.pred_range = np.arange(args.r1, args.r2)

    print(config.Train_set_path)
    IS_Training = True
    if IS_Training:
        train(config)
    else:
        test(config)
main()

