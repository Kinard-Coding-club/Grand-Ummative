# Makefile to compile .bat to .exe

# Define the batch file and the desired output exe
BAT_FILE=start_game.bat
EXE_NAME=start_game.exe

# Path to Advanced BAT to EXE Converter (adjust if needed)
EXE_CONVERTER_PATH="C:/Program Files/Advanced BAT to EXE Converter/AdvancedBATtoEXEConverter.exe"

# Default target to compile the batch file to exe
all: $(EXE_NAME)

# Rule to compile .bat file to .exe
$(EXE_NAME): $(BAT_FILE)
	$(EXE_CONVERTER_PATH) /bat "$(BAT_FILE)" /exe "$(EXE_NAME)" /silent /icon "game_icon.ico" /unhide

# Clean up generated exe file
clean:
	rm -f $(EXE_NAME)
