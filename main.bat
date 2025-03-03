echo ----- Game start -----
echo using NT kernel
python -version
pip --version >nul 2>&1
if %errorlevel% neq 0 (
	echo pip is not installed
    mshta "javascript:alert('Python is not installed.');close()"
	exit /b 1
) else (
	echo pip version is satisfactory
)
echo python version is satasfactory
pip --version >nul 2>&1
if %errorlevel% neq 0 (
	echo pip is not installed
    mshta "javascript:alert('pip is not installed.');close()"
	exit /b 1
) else (
	echo pip version is satisfactory
)
python3 main.py