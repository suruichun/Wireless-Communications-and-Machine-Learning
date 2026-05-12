@echo off
echo 正在開始批次執行測試...

python .\Main.py --Pilots 64 --SNR 25 --mu 6
python .\Main.py --Pilots 16 --SNR 25 --mu 6
python .\Main.py --Pilots 8 --SNR 25 --mu 6

python .\Main.py --Pilots 64 --SNR 10 --mu 6
python .\Main.py --Pilots 16 --SNR 10 --mu 6
python .\Main.py --Pilots 8 --SNR 10 --mu 6

python .\Main.py --Pilots 64 --SNR 15 --mu 6
python .\Main.py --Pilots 16 --SNR 15 --mu 6
python .\Main.py --Pilots 8 --SNR 15 --mu 6

python .\Main.py --Pilots 64 --SNR 20 --mu 6
python .\Main.py --Pilots 16 --SNR 20 --mu 6
python .\Main.py --Pilots 8 --SNR 20 --mu 6

python .\Main.py --Pilots 64 --SNR 5 --mu 6
python .\Main.py --Pilots 16 --SNR 5 --mu 6
python .\Main.py --Pilots 8 --SNR 5 --mu 6

echo 所有任務已完成！
pause