@echo off
echo ----- Engine 1.0.0 installer -----
echo This will install the game engine.
echo Contents
echo 1. Python
echo 2. PIP
echo 3. Pygame
choice /C YN /M "Do you want to continue with the installation?"
if errorlevel 2 goto end
echo installing Python...
set PYTHON_INSTALLER_URL=https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe
set INSTALLER_PATH=%TEMP%\python_installer.exe
echo installing PIP...
python -m get-pip
echo installing required packages...
pip install pygame

echo --- Game installed! ---
echo You may now close this window.
pause
:end
echo Aborted. You may now close this window.