import zipfile

def zipping_file_predef():
    zip_input = input("\nWould you like to zip the text file, which includes the word sentence and positions, so that it takes up less space?  [Yes/No]  ")
    zip_input_lower = zip_input.lower()

    if zip_input_lower == "yes":
        zipname_input = input("What would you like the zipped filename to be:  ")
        zipname_input = zipname_input + ".zip"

        zipping_file = zipfile.ZipFile(zipname_input, "a")
        zipping_file.write(filewrite_name)
        zipping_file.close()

        print("\nCongratulations " + username + "!!! You have written the sentence list and the position list to the file: " + zipname_input)
        reading_file_predef()

