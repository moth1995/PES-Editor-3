from editor.option_file import OptionFile

# Put PES 5 Option File in the same folder as this script
#of_file_location = "KONAMI-WIN32PES4OPT"
of_file_location = r"D:\Juegos\KONAMI\Pro Evolution Soccer 4\save\folder1\KONAMI-WIN32PES4OPT"

# Load/decrypt the option file
print("Loading option file...")
of = OptionFile(of_file_location)
print("Option file loaded.")

with open("temp.bin", "rb") as binary_file:
    of.data = bytearray(binary_file.read())
# Save/encrypt the option file
print("Saving option file...")
of.save_option_file()
print("Option file saved.")
