user_sentence = input("Please enter a sentence that you would like to see the position of the words:  ")
user_sentence_lower = user_sentence.lower()
user_sentence_list = user_sentence_lower.split()

def predef_custom_word_pos():
    user_word_position = [user_sentence_list.index(x)+1 for x in user_sentence_list]
    print (user_word_position)

user_input = input("\nWould you like to see the positions of the words [Yes/No]:  ")
user_input_lower = user_input.lower()

if user_input_lower == "yes":
    print ("\nHere you go, this is the position of each word in the sentence:")
    predef_custom_word_pos()
elif user_input_lower == "no":
    print("\nGoodbye, hope we see you again.")
