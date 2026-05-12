@echo off
echo 正在開始批次執行測試...

python .\Main.py --Pilots 64 --SNR 5 --r1 0 --r2 16
python .\Main.py --Pilots 64 --SNR 5 --r1 32 --r2 48
python .\Main.py --Pilots 64 --SNR 5 --r1 48 --r2 64
python .\Main.py --Pilots 64 --SNR 5 --r1 64 --r2 80
python .\Main.py --Pilots 64 --SNR 5 --r1 80 --r2 96
python .\Main.py --Pilots 64 --SNR 5 --r1 96 --r2 112
python .\Main.py --Pilots 64 --SNR 5 --r1 112 --r2 128


echo 所有任務已完成！
pause