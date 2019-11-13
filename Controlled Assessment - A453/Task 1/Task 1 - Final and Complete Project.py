"""
The first thing the user is greeted with is the code below, which outputs/prints
a statement which says Good Morning, Good Afternoon or Good Evening based on
what time of day the user is executing the code.
"""

import datetime
now = datetime.datetime.now()
now = now.hour

if now < 12:
    print ("Good Morning Sir/Madam ☜(⌒▽⌒)☞, \n")
elif 12 <= now < 18:
    print("Good Afternoon Sir/Madam ☜(⌒▽⌒)☞, \n")
else:
    print ("Good Evening Sir/Madam ☜(⌒▽⌒)☞, \n")

"""
The code then requires the user to input their name and state whether they
have used the program before and outputs/prints a response based on their input.
"""
username = input("What is your name ¯\(°_O)/¯ ? ")

visit = input("\nHave you been here before " + username + " ╚(ಠ_ಠ)=┐ ? [Yes/No] ")
visit_uppercase = visit.upper()

if visit_uppercase == "YES":
    print ("\nWelcome back to Position Finder " + username + ", make sure you have fun. (｡◕‿◕｡)")
elif visit_uppercase == "NO":
    print ("\nHi ", username, ",", " Welcome to Position Finder. (｡◕‿◕｡)")

print("\n┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴")

input("\nPress Enter to continue...")

"""
This piece of the code allows the user to choose one of the programs three
functions, 1. Find the position of a word in a premade sentence, 2. Find the
word in the users own custom sentence or 3. Exit the program, and then based
on what the user want's to
do, the program will execute thepecific section of
code.  The code is in a while loop, which allows the user to choose any function
an infinite amount of times without error.
"""
pos_finder_func = True

while pos_finder_func:
    print ("\nPosition Finder Functions Include ( ﾟдﾟ)､: \n\n1. Find the position of a word in a premade sentence. \n2. Find the position of a word in your own custom sentence. \n3. Exit.")
    pos_finder_func = input("\nPick one of the functions above ^^^ :  ")

    if pos_finder_func == "1":
        premade = "\nThe premade sentence of the day is: "
        sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
        print (premade + sentence)
        sentence_uppercase = sentence.upper()
        sentence_list = sentence_uppercase.split(' ')

        user_input = input("\nWhat word would you like to find the position of from the sentence? (Notice: One word only) ^^^ :  ")
        user_input_uppercase = user_input.upper()

        word_not_in_sentence = "N"

        for (i, word) in enumerate(sentence_list):
            if (word == user_input_uppercase):
                print ("\nThere are", len(sentence_list), "words in the sentence and the word '" + user_input + "' is in position: ", i+1)
                word_not_in_sentence = "Y"

        if word_not_in_sentence == "N":
            print("\nIm sorry " + username + " the word '" + user_input + "' isn't in the sentence.")

        input("\nPress Enter to continue...")
        print("\nTo remind you:")

    elif pos_finder_func == "2":
        user_sentence = input("\nWhat is your custom sentence: ")
        user_sentence_uppercase = user_sentence.upper()
        user_sentence_list = user_sentence_uppercase.split(' ') 

        user_sentence_input = input("\nWhat word would you like to find the position of in your sentence? (Notice: One word only) ^^^ :  ")
        user_sentence_input_uppercase = user_sentence_input.upper()

        word_not_in_sentence = "N"

        for (i, word) in enumerate(user_sentence_list):
            if (word == user_sentence_input_uppercase):
                print ("\nThere are", len(user_sentence_list), "words in the sentence and the word '" + user_sentence_input + "' is in position: ", i+1)
                word_not_in_sentence = "Y"

        if word_not_in_sentence == "N":
            print("\nIm sorry " + username + ", the word '" + user_sentence_input + "' isn't in the sentence.")

        input("\nPress Enter to continue...")
        print("\nTo remind you:")
        
    if pos_finder_func == "3":
        print ("\nGoodbye, hope we see you again.  ಠ‿↼")
        import sys
        sys.exit()
