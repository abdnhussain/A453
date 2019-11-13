
# First it was like this.

sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
sentence_uppercase = sentence.upper()
sentence_list = sentence_uppercase.split()

word_position = [sentence_list.index(x)+1 for x in sentence_list]
word_position_str = str(word_position)

filewrite = open("Word positions", "a")
filewrite.write(word_position_str)
filewrite.close()


# Then it was like this.

sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
sentence_uppercase = sentence.upper()
sentence_list = sentence_uppercase.split()

word_position = [sentence_list.index(x)+1 for x in sentence_list]
word_position_str = str(word_position)

filewrite = open("Word positions.txt", "a")
filewrite.write(word_position_str)
filewrite.close()
