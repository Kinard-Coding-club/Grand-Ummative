echo ---- Installing game ----
echo this script will require sudo privileges throughout the installation process.
sudo apt install python3 python3-venv
python3 -m ensurepip
pip install -r requirements.txt
curl https://adrian.elipson.dev/2025codlingclub/2025codlingclub.zip -o 2025codlingclub.zip
unzip 2025codlingclub.zip
rm 2025codlingclub.zip
mv 2025codlingclub monkeyland
echo "The following operation requires sudo."
sudo mv monkeyland /usr/local/games/
echo "The following operation requires sudo."
sudo chmod +x /usr/local/games/monkeyland/main.sh

# Create a .desktop file
echo "Creating .desktop file for the game..."
cat <<EOF > /tmp/monkeyland.desktop
[Desktop Entry]
Name=Monkeyland
Exec=/usr/local/games/monkeyland/main.sh
Icon=/usr/local/games/monkeyland/icon.png
Type=Application
Categories=Game;
EOF

echo "The following operation requires sudo."
sudo mv /tmp/monkeyland.desktop /usr/share/applications/monkeyland.desktop
echo "Installation complete. You can now find Monkeyland in your start menu."