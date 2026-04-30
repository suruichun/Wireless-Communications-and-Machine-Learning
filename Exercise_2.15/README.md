# Exercise 2.15: CSI Compression and Reconstruction using CsiNet and CS-CsiNet

Before run the codes, please download the data in https://www.dropbox.com/scl/fo/tqhriijik2p76j7kfp9jl/h?rlkey=4r1zvjpv4lh5h4fpt7lbpus8c&e=1&dl=0 from “Deep learning for massive MIMO CSI feedback". (GitHub: https://github.com/sydney222/Python_CsiNet)


## File Structure

| File / Directory | Purpose |
|------|---------|
| `CsiNet_train.py` | CsiNet training pipeline: model building, training, evaluation, saving. |
| `CsiNet_onlytest.py` | CsiNet inference only: load pre-trained model, reconstruct CSI, evaluate. |
| `CS-CsiNet_train.py` | CS-CsiNet training pipeline: train decoder with fixed CS encoder. |
| `CS-CsiNet_onlytest.py` | CS-CsiNet inference only: load decoder, reconstruct CSI from compressed data. |
| `data/` | Directory containing MATLAB-formatted CSI datasets and random projection matrices. |
| `result/` | Output directory containing training logs, loss curves, reconstructed data, model checkpoints, pre-trained model architectures (`.json`), weights (`.h5`) for inference and visulized reconstruction result. |

---

## Evaluation

Run CsiNet_onlytest.py or CS-CsiNet_onlytest.py

## Training

Run CsiNet_train.py or CS-CsiNet_train.py
