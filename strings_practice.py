 # 1

name = "Jimdandy"

print(name[0])
print(name[-1])
print(name[2:5])

# 2

print(name[::-1])

# 3

message = "   Hello WORLD   "

print(message.strip().lower())

# 4

sentence = "Hi, how are you?"

print(len(sentence.split()))

# 5

words = ["Jim", "is", "gwapo."]
print(",".join(words))

# 6

# name = "Jimdandy"
# name[0] = "X"

# TypeError: 'str' object does not support item assignment. String are immutable, you cannot change a character. 

# 7

def find(sentence, word):
  if word in sentence:
    return True
  else: 
    return False

result = find("Jim is gwapo.", "gwapo")
print(result)
result = find("Jim is gwapo.", "kaayo")
print(result)