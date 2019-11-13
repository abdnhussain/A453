import zipfile

def reading_file_predef():
    extract_input = input("\nWould you like to read the text in the file that you just created and compressed?  [Yes/No]  ")
    extract_input_lower = extract_input.lower()

    if extract_input_lower == "yes":
        file_read = input("What text file would you like to read:  ")
        file_read = file_read + ".txt"
        
        reading = open(file_read, "r")
        print("\nThis is all that is in the text file '" + file_read + "': \n" + reading.read())
