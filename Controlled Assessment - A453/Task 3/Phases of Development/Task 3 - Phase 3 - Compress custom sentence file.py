import zipfile

def zipping_file_custom():
    zip_input = input("\nWould you like to zip the text file, which includes the word sentence and positions, so that it takes up less space?  [Yes/No]  ")
    zip_input_lower = zip_input.lower()

    if zip_input_lower == "yes":
        user_zipname_input = input("What would you like the zipped filename to be:  ")
        user_zipname_input = user_zipname_input + ".zip"

        user_zipping_file = zipfile.ZipFile(user_zipname_input, "a")
        user_zipping_file.write(user_filewrite_name)
        user_zipping_file.close()

        print("\nCongratulations " + username + "!!! You have written the sentence list and the position list to the file: " + user_zipname_input)
        reading_file_custom()
