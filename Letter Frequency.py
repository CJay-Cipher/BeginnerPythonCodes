
# def letter_frequency(word,letter):

#     word_length = len(word)
#     count_letter = word.count(letter)
#     return (count_letter/word_length) * 100
    
# word = input("Type in the word: ").lower()
# letter = input("Type in the letter to check frequency: ").lower()

# print(letter_frequency(word , letter))

# def add_dots(the_word):
#     the_word = list(the_word)
#     for letters in range(len(the_word)):
#         the_word[letters] = the_word[letters] + "."
#     return (''.join(the_word))

# def remove_dots(word):
#     word = list(word)
#     for items in word:
#         word.remove(".")
#     return (''.join(word))

# the_word = input("what is the word?\n")

# dot_the_word = add_dots(the_word)

# # print(f"The word with the dots added is: {dot_the_word}")
# print(f"The word with the dots removed is: {remove_dots(dot_the_word)}")

def remove_space_and_sort(words):
    words = words.split(" ")
    for words in words:
        words.sort()
        print()
        if words.count(words) > 1:
            words.remove(words)
    words = ' '.join(words)
    print(type(words))
    return words


sentence = input("Enter the words\n").lower()
print(remove_space_and_sort(sentence))