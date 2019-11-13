"""
# First it was like this.

sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
sentence_uppercase = sentence.upper()
sentence_list = sentence_uppercase.split()
print (sentence)

for (i, word) in enumerate(sentence_list):
    print(i+1)

"""
"""
# Then it was like this.

sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
sentence_uppercase = sentence.upper()
sentence_list = sentence_uppercase.split()
print (sentence)

for x in sentence_list:
    word_position = sentence_list.index(x)+1
    print(word_position)
"""
# Finally it was like this.

sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
sentence_uppercase = sentence.upper()
sentence_list = sentence_uppercase.split()
print (sentence)

word_position = [sentence_list.index(x)+1 for x in sentence_list]
print (word_position)
