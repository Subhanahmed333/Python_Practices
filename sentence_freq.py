from collections import Counter
sentence = input("Enter a sentence: ")
sentence = sentence.lower()
sentence = sentence.split()
sentence = Counter(sentence)
print(sentence)