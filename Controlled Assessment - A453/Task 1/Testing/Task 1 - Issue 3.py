# First it was like this.

print ("\nPosition Finder Functions Include ( ﾟдﾟ)､: \n\n1. Find the position of a word in a premade sentence. \n2. Find the position of a word in your own custom sentence. \n3. Exit.")
pos_finder_func = input("\nPick one of the functions above ^^^ : ")

while pos_finder_func == "1" or pos_finder_func == "2" or pos_finder_func == "3":

    if pos_finder_func == "1":
        premade = "\nThe premade sentence of the day is: "
        sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
        print (premade + sentence)
        sentence_uppercase = sentence.upper()
        sentence_list = sentence_uppercase.split(' ')

        user_input = input("\nWhat word would you like to find the position of from the sentence? (Notice: One word only) ^^^ : ")
        user_input_uppercase = user_input.upper()

        word_not_in_sentence = "N"

        for (i, word) in enumerate(sentence_list):
            if (word == user_input_uppercase):
                print ("\nThere are",len(sentence_list),"words in the sentence and the word '"+ user_input +"' is in position: " ,i+1)
                word_not_in_sentence = "Y"

        if word_not_in_sentence == "N":
            print("\nIm sorry, the word '"+ user_input +"' isn't in the sentence.")

        input("\nPress Enter to continue...")
        print("\nTo remind you:")

    elif pos_finder_func == "2":
        user_sentence = input("\nWhat is your custom sentence: ")
        user_sentence_uppercase = user_sentence.upper()
        user_sentence_list = user_sentence_uppercase.split(' ') 

        user_sentence_input = input("\nWhat word would you like to find the position of in your sentence? (Notice: One word only):")
        user_sentence_input_uppercase = user_sentence_input.upper()

        word_not_in_sentence = "N"

        for (i, word) in enumerate(user_sentence_list):
            if (word == user_sentence_input_uppercase):
                print ("\nThere are",len(user_sentence_list),"words in the sentence and the word '"+ user_sentence_input +"' is in position: " ,i+1)
                word_not_in_sentence = "Y"

        if word_not_in_sentence == "N":
            print("\nIm sorry, the word '"+ user_sentence_input +"' isn't in the sentence.")

        input("Press Enter to continue...")
        print("\nTo remind you:")
        
    if pos_finder_func == "3":
        print ("\nGoodbye, hope we see you again.  ಠ‿↼")
        import sys
        sys.exit()

# Then it was like this.

pos_finder_func = True

while pos_finder_func:
    print ("\nPosition Finder Functions Include ( ﾟдﾟ)､: \n\n1. Find the position of a word in a premade sentence. \n2. Find the position of a word in your own custom sentence. \n3. Exit.")
    pos_finder_func = input("\nPick one of the functions above ^^^ : ")

    if pos_finder_func == "1":
        premade = "\nThe premade sentence of the day is: "
        sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
        print (premade + sentence)
        sentence_uppercase = sentence.upper()
        sentence_list = sentence_uppercase.split(' ')

        user_input = input("\nWhat word would you like to find the position of from the sentence? (Notice: One word only) ^^^ : ")
        user_input_uppercase = user_input.upper()

        word_not_in_sentence = "N"

        for (i, word) in enumerate(sentence_list):
            if (word == user_input_uppercase):
                print ("\nThere are",len(sentence_list),"words in the sentence and the word '"+ user_input +"' is in position: " ,i+1)
                word_not_in_sentence = "Y"

        if word_not_in_sentence == "N":
            print("\nIm sorry, the word '"+ user_input +"' isn't in the sentence.")

        input("\nPress Enter to continue...")
        print("\nTo remind you:")

    elif pos_finder_func == "2":
        user_sentence = input("\nWhat is your custom sentence: ")
        user_sentence_uppercase = user_sentence.upper()
        user_sentence_list = user_sentence_uppercase.split(' ') 

        user_sentence_input = input("\nWhat word would you like to find the position of in your sentence? (Notice: One word only):")
        user_sentence_input_uppercase = user_sentence_input.upper()

        word_not_in_sentence = "N"

        for (i, word) in enumerate(user_sentence_list):
            if (word == user_sentence_input_uppercase):
                print ("\nThere are",len(user_sentence_list),"words in the sentence and the word '"+ user_sentence_input +"' is in position: " ,i+1)
                word_not_in_sentence = "Y"

        if word_not_in_sentence == "N":
            print("\nIm sorry, the word '"+ user_sentence_input +"' isn't in the sentence.")

        input("Press Enter to continue...")
        print("\nTo remind you:")
        
    if pos_finder_func == "3":
        print ("\nGoodbye, hope we see you again.  ಠ‿↼")
        import sys
        sys.exit()
        

