import zipfile

def reading_file_custom():
    extract_input = input("\nWould you like to read the text in the file that you just created and compressed?  [Yes/No]  ")
    extract_input_lower = extract_input.lower()

    if extract_input_lower == "yes":
        user_file_read = input("What text file would you like to read:  ")
        user_file_read = user_file_read + ".txt"
        
        user_reading = open(user_file_read, "r")
        print("\nThis is all that is in the text file '" + user_file_read + "': \n" + user_reading.read())
