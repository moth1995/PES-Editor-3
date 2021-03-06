from editor.option_file import OptionFile

# Put PES 3 Option File in the same folder as this script
of_file_location = r"KONAMI-WIN32PES3OPT"

# Load/decrypt the option file
print("Loading option file...")
of = OptionFile(of_file_location)
print("Option file loaded.")

with open("temp.bin", "wb") as binary_file:
    binary_file.write(of.data)