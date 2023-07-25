"""
CP1404/CP5632 Practical 05
Wimbledon data-reading, processing and displaying
Word Occurrences
Estimate: 35 minutes
Actual:   50 minutes

"""
text = input("Text: ")
# testing
# print(text)
words = text.split()
words.sort()
# testing
# print(words)
word_to_frequency = {}
for word in words:
    # check if word is a key or not
    if word in word_to_frequency:
        word_to_frequency[word] += 1
    else:  # new key
        word_to_frequency[word] = 1
# max len of words - list comprehension
max_length = max((len(word) for word in words))
for word in word_to_frequency:
    print(f"{word:{max_length}} {word_to_frequency[word]}")
