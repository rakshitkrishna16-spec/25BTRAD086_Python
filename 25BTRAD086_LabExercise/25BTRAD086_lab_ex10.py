text = "python is easy and python is fun"
words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word Frequencies:")
for word, count in freq.items():
    print(f"{word}: {count}")