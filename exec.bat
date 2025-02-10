@echo off
echo --- Game checksum ---

:: Check if pip is installed and has a version
echo is PIP installed?
for /f "tokens=*" %%a in ('pip --version 2^>nul') do set PIP_VERSION=%%a
if not defined PIP_VERSION (
    cls
    echo Missing requirements! Please reinstall!
    exit /b
) else (
    echo %PIP_VERSION%
)

:: Check if Python is installed and has a version
echo is python installed?
for /f "tokens=*" %%b in ('python --version 2^>nul') do set PYTHON_VERSION=%%b
if not defined PYTHON_VERSION (
    cls
    echo Missing requirements! Please reinstall!
    exit /b
) else (
    echo %PYTHON_VERSION%
)

echo Passed.
python3 main.py
