#  /* Copyright © Wheelers Lane Technology College - All Rights Reserved
#   * Unauthorized copying of this file, via any medium is strictly prohibited
#   * Proprietary and confidential
#   * Written by Abdullah Hussain <12hussaina1@wheelerslane.co.uk>, December 2016
#   */

'''
This part of the code imports the date and time, and based on the time of day outputs a
greeting message.
'''

import datetime
now = datetime.datetime.now()
now = now.hour

if now < 12:
    print ("Good Morning Sir/Madam ☜(⌒▽⌒)☞, \n")
elif 12 <= now < 18:
    print("Good Afternoon Sir/Madam ☜(⌒▽⌒)☞, \n")
else:
    print ("Good Evening Sir/Madam ☜(⌒▽⌒)☞, \n")

'''
This part of the code prompts the user to enter their name and state whether or not they
have used the program before and outputs a response based on their input.
'''

username = input("What is your name ¯\(°_O)/¯ ? ")

visit = input("\nHave you been here before " + username + " ╚(ಠ_ಠ)=┐ ? [Yes/No] ")
visit_lower = visit.lower()

if visit_lower == "yes":
    print ("\nWelcome back to Word Positioner " + username + ", make sure you have fun. (｡◕‿◕｡)")
elif visit_lower == "no":
    print ("\nHi ", username, ",", " Welcome to Word Positioner. (｡◕‿◕｡)")

print("\n┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴")

input("\nPress Enter to continue...")

'''
This piece of the code allows the user to choose one of the programs three functions, and
then based on the input, the program will execute the specific section of code.  The code
is in a while loop, which allows the user to choose any function an infinite amount of
times without error.
'''

menu = True

while menu:
    print("\nWord Positioner Functions Include:  \n\n1. View the positions of the words in a predefined sentence. \n2. View the positions of the words in your own custom sentence. \n3. Exit.")
    menu = input("\nPick one of the functions above ^^^ :  ")

    if menu == "1":
        premade = "\nThe premade sentence of the day is: "
        sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
        sentence_uppercase = sentence.upper()
        sentence_list = sentence_uppercase.split()
        print (premade+sentence)

        def predef_word_pos():
            word_position = [sentence_list.index(x)+1 for x in sentence_list]
            print (word_position)

        user_input = input("\nWould you like to see the positions of the words [Yes/No]:  ")
        user_input_lower = user_input.lower()

        if user_input_lower == "yes":
            print ("\nHere you go, this is the position of each word in the sentence:")
            predef_word_pos()

            write_input = input("\nWould you like to write this to an external file? [Yes/No] ")
            write_input_lower = write_input.lower()

            if write_input_lower == "yes":
                filename_input = input("What would you like the file name to be:  ")

                word_position = [sentence_list.index(i)+1 for i in sentence_list]
                word_position_str = str(word_position)
    
                filewrite = open(filename_input + ".txt", "a")
                filewrite.write("Predefined Sentence (" + username + ")" + "\nThis is the sentence '" + sentence + "'  \nThese are the word positions:  " +word_position_str + "\n\n")
                filewrite.close()

                print("\nCongratulations " + username + "!!! You have wrote the sentence list and the position list to the file: " + filename_input)

                input("\nPress Enter to continue...")
                print("\nTo remind you:")
            
            elif write_input_lower == "no":
                input("\nPress Enter to continue...")
                print("\nTo remind you:")

        elif user_input_lower == "no":
            input("\nPress Enter to continue...")
            print("\nTo remind you:")

    elif menu == "2":
        user_sentence = input("\nPlease enter a sentence that you would like to see the position of the words:  ")
        user_sentence_lower = user_sentence.lower()
        user_sentence_list = user_sentence_lower.split()

        def predef_custom_word_pos():
            user_word_position = [user_sentence_list.index(i)+1 for i in user_sentence_list]
            print (user_word_position)

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
    
                filewrite = open(user_filename_input + ".txt", "a")
                filewrite.write("Custom Sentence (" + username + ")" + "\nThis is the sentence:  '" + user_sentence + "' \nThese are the word positions:  " +user_word_position_str + "\n\n")
                filewrite.close()
                
                print("\nCongratulations " + username + "!!! you have wrote the sentence list and the position list to the file: " + user_filename_input)

                input("\nPress Enter to continue...")
                print("\nTo remind you:")

            elif write_input_lower == "no":
                input("\nPress Enter to continue...")
                print("\nTo remind you:")

        elif user_input_lower == "no":
            input("\nPress Enter to continue...")
            print("\nTo remind you:")

    elif menu == "3":
        print ("\nGoodbye, hope we see you again.")
        import sys
        sys.exit()
