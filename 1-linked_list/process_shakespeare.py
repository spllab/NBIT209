# Author PAUL OFFEI
# Date: 4/10/2023
# Program Description: Cleaning a File from lines sentences to word of line

least_word_size = 5

read_file = open("shakespeare.txt", "r")
for line in read_file:
    sentence = line.strip()
    word_bag = sentence.split()

    for word in word_bag:
        lowercase_word = word.lower()
        lowercase_word = lowercase_word.strip("[")
        lowercase_word = lowercase_word.strip("]")
        lowercase_word = lowercase_word.strip("#")
        lowercase_word = lowercase_word.strip(".")
        lowercase_word = lowercase_word.strip(",")
        lowercase_word = lowercase_word.strip(":")
        lowercase_word = lowercase_word.strip("`")
        lowercase_word = lowercase_word.strip("?")
        lowercase_word = lowercase_word.strip("(")
        lowercase_word = lowercase_word.strip(")")
        lowercase_word = lowercase_word.strip(";")
        lowercase_word = lowercase_word.strip("'")
        if len(lowercase_word) >= least_word_size:
            clean_word = lowercase_word
            write_file = open("shakespeare_cleaned.txt", "a")
            write_file.write(clean_word + "\n")
            write_file.close()
read_file.close() 