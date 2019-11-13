'''
This piece of code stores a predefined sentence in a variable and prints it to
the user as well as splitting the sentence into a list and storing that in a
variable.
'''

premade = "The premade sentence of the day is: "
sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
sentence_uppercase = sentence.upper()
sentence_list = sentence_uppercase.split()
print (premade+sentence)

'''
This piece of code defines a function which finds the position of the words in
the predefined sentence even if it's repeated.
'''

def predef_word_pos():
    word_position = [sentence_list.index(x)+1 for x in sentence_list]
    print (word_position)

"""
This piece of code asks the user if they would
like to see the positions of the words in the sentence
and then based on their input, it either calls upon the function (predef_word_pos) created earlier or
simply prints Goodbye and exits the program.
"""

user_input = input("\nWould you like to see the positions of the words [Yes/No]:  ")
user_input_lower = user_input.lower()

if user_input_lower == "yes":
    print ("\nHere you go, this is the position of each word in the sentence:")
    predef_word_pos()

    write_input = input("\nWould you like to write this to an external file? [Yes/No] ")
    write_input_lower = write_input.lower()

    if write_input_lower == "yes":
        filename_input = input("What would you like the file name to be:  ")

        word_position = [sentence_list.index(x)+1 for x in sentence_list]
        word_position_str = str(word_position)
    
        filewrite = open(filename_input, "a")
        filewrite = filewrite.write("This is the sentence:  '" + sentence + "' and this is the word positions:  " +word_position_str + "\n")
        filewrite.close()

        print("\nCongratulations, you have wrote the sentence list and the position list to the file: " + filename_input)

    elif write_input_lower == "no":
        print ("\nGoodbye, hope we see you again.")
        import sys
        sys.exit()

elif user_input_lower == "no":
    print ("\nGoodbye, hope we see you again.")
    import sys
    sys.exit()

