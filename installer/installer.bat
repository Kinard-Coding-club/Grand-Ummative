@echo off
echo ----- installing game -----
python -m ensurepip
pip install -r requirements.txt
curl https://adrian.elipson.dev/codingclub/kinard2025/download/?install=False
