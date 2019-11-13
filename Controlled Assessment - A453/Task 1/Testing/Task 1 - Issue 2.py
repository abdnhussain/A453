
# First it was like this.

user_sentence = input("\nWhat is your custom sentence: ")
user_sentence_uppercase = user_sentence.upper()
user_sentence_list = user_sentence_uppercase.split(' ') 

user_sentence_input = input("\nWhat word would you like to find the position of in your sentence? (Notice: One word only) ^^^ :  ")
user_sentence_input_uppercase = user_sentence_input.upper()

word_not_in_sentence = "N"

for (i, word) in enumerate(user_sentence_list):
    if (word == user_sentence_input_uppercase):
        print ("\nThere are", len(user_sentence_list), "words in the sentence and the word '" + user_sentence_input + "' is in position: ", i+1)
    else:
        print ("Im sorry the word isn't in the sentence")

# Then it was like this.

user_sentence = input("\nWhat is your custom sentence: ")
user_sentence_uppercase = user_sentence.upper()
user_sentence_list = user_sentence_uppercase.split(' ') 

user_sentence_input = input("\nWhat word would you like to find the position of in your sentence? (Notice: One word only) ^^^ :  ")
user_sentence_input_uppercase = user_sentence_input.upper()

word_not_in_sentence = "N"

for (i, word) in enumerate(user_sentence_list):
    if (word == user_sentence_input_uppercase):
        print ("\nThere are", len(user_sentence_list), "words in the sentence and the word '" + user_sentence_input + "' is in position: ", i+1)
        break
    else:
        print ("Im sorry the word isn't in the sentence")
        break

# Finally it was like this.

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
    print("\nIm sorry, the word '" + user_sentence_input + "' isn't in the sentence.")
