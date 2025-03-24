from collections import Counter
characters = input("Enter the characters: ")
characters = characters.lower().strip()
characters = Counter(characters)
count = []
for i in characters:
    if characters[i] == 1:
        count.append(i)
print(count)