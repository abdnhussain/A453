premade = "The premade sentence of the day is: "
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
    print("\nHere you go, this is the position of each word in the sentence:")
    predef_word_pos()
elif user_input_lower == "no":
    print("\nGoodbye, hope we see you again.")

