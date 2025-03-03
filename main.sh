echo ----- Running game... -----
python3 -version
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3 to continue."
    response=$(zenity --question --text="Python is not installed. Do you want to install it now?" --ok-label="Yes" --cancel-label="No"; echo $?)
    echo "User response: $response" >> response.log
    if [ "$response" -eq 0 ]; then
        sudo apt install python3 python3-venv
        python3 -m ensurepip
        pip install -r requirements.txt
    else
        echo "User declined request."
    fi
fi
python3 main.py