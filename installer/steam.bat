@echo off
echo --- Installing game, expect other windows... ---
set PYTHON_INSTALLER_URL=https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe
set INSTALLER_PATH=%TEMP%\python_installer.exe
set GAME_URL=https://www.wonk.app/game.zip
set GAME_PATH=%TEMP%\game.zip

echo Step 1/7 ----- Downloading Python installer...
powershell -Command "Invoke-WebRequest -Uri %PYTHON_INSTALLER_URL% -OutFile %INSTALLER_PATH%"

echo Step 2/7 Installing Python...
start /wait %INSTALLER_PATH% /quiet InstallAllUsers=1 PrependPath=1

echo Step 3/7 Installing pip...
powershell -Command "Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://bootstrap.pypa.io/get-pip.py'))"

echo Step 4/7 Installing required packages...
pip install -r requirements.txt

echo Step 5/7 Installing game...
powershell -Command "Invoke-WebRequest -Uri %GAME_URL% -OutFile %GAME_PATH%"

echo Step 6/7 Extracting game...
powershell -Command "Expand-Archive -Path %GAME_PATH% -DestinationPath %TEMP%\game"

echo Step 7/7 Cleaning up...
del %INSTALLER_PATH%
del %GAME_PATH%

echo --- Game installed! ---
echo You may now close this window.
pause