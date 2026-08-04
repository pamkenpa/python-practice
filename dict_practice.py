ages = {"Jim": 26, "Anna": 30, "Leo": 40, "Isa": 29}

for name, age in ages.items():
    if age >= 30:
        print(name, "is", age, "years old")

word = "banana"
letter_counts = {}

for letter in word:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

print(letter_counts)

word = "mississippi"
letter_counts = {}

for letter in word:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

print(letter_counts)

sentence = "the cat sat on the mat the cat ran"

print(sentence.split())

word_counts = {}

for word in sentence.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)


for word, count in word_counts.items():
    if count > 1:
        print(word)

word_counts = {"the": 3, "cat": 2, "sat": 1}

most_common_word = None
highest_count = 0

for word, count in word_counts.items():
    if count > highest_count:
        highest_count = count
        most_common_word = word

print(most_common_word, highest_count)


word_counts = {"the": 3, "cat": 2, "sat": 1}


def most_common(word_counts):
    most_common_word = None
    highest_count = 0
    for word, count in word_counts.items():
        if count > highest_count:
            highest_count = count
            most_common_word = word
            
    return most_common_word

result = most_common(word_counts)
print(result)






