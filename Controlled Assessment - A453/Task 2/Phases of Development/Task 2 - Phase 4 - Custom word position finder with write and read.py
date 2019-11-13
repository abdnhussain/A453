'''
This piece of code prompts the user to enter a sentence, stores it in a variable, splits the sentence into a list and stores that in a
variable.
'''

user_sentence = input("Please enter a sentence that you would like to see the position of the words:  ")
user_sentence_lower = user_sentence.lower()
user_sentence_list = user_sentence_lower.split()

'''
This piece of code defines a function which finds the position of the words in
the user inputed sentence even if it's repeated.
'''

def predef_custom_word_pos():
    user_word_position = [user_sentence_list.index(i)+1 for i in user_sentence_list]
    print (user_word_position)

"""
This piece of code asks the user if they would like to see the positions of the words in the sentence
and then based on their input, it either calls upon the function (predef_custom_word_pos) created earlier or
simply prints Goodbye and exits the program.
"""

user_input = input("\nWould you like to see the positions of the words [Yes/No]:  ")
user_input_lower = user_input.lower()

if user_input_lower == "yes":
    print ("\nHere you go, this is the position of each word in the sentence:")
    predef_custom_word_pos()

    write_input = input("\nWould you like to write this to an external file? [Yes/No] ")
    write_input_lower = write_input.lower()


    if write_input_lower == "yes":
        user_filename_input = input("What would you like the file name to be:  ")

        user_word_position = [user_sentence_list.index(i)+1 for i in user_sentence_list]
        user_word_position_str = str(user_word_position)
    
        filewrite = open(user_filename_input, "a")
        filewrite = filewrite.write("This is the sentence:  '" + user_sentence + "' and this is the word positions:  " +user_word_position_str + "\n")

        print("\nCongratulations, you have wrote the sentence list and the position list to the file: " + user_filename_input)

    elif write_input_lower == "no":
        print ("\nGoodbye, hope we see you again.")
        import sys
        sys.exit()

else:
    print ("\nGoodbye, hope we see you again.")
    import sys
    sys.exit()

