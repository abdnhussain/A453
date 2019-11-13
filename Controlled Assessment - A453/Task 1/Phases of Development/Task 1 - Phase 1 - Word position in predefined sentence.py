
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

if word_not_in_sentence == "N":
    print("\nIm sorry the word '" + user_input + "' isn't in the sentence.")
