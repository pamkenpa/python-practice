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

result = count_words(text.lower().strip("."))
print(result)

counts = result

def most_common(counts):
  most_common_word = None
  highest_count = 0
  for word, count in result.items():
	    if count > highest_count:
             highest_count = count
             most_common_word = word
  return most_common_word

# result = most_common(counts)
# print(result)



def longest_word(result):
  for word in result():
      word = None
      longest = result[word]
      if len(word) > longest:
         longest = word
  return longest

result = longest_word(result)
print(result)
      
      
      
   

      
      












  




