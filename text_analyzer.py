text = input("Enter a paragraph: ")


def word_count(text):
  count = 0
  for word in text.split():
    count += 1
  return count

# result = word_count(paragraph)
# print(result)


def char_count(text):
  count = len(text)
  for character in text:
    if character == " ":
      count -= 1
  return count
    
# result = char_count(text)
# print(result)


def count_words(text):
  count = {}
  for word in text.split():

    if word in count:
      count[word] += 1
    else:
      count[word] = 1
  return count

result = count_words(text)
print(result)





  




