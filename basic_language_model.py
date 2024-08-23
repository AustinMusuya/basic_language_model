import random
filename = './text.txt'

reader = open(filename, 'r', encoding='utf-8')
punctuation = '.;,-“’”:?—‘!()_'

# lines =  reader.readlines()

# Create array of words in line 1

# word_list = lines[5].split()
from collections import Counter
successor_map = {}
window = []
bigram_counter = Counter()

# for line in reader:
#   for word in line.split():
#     cleaned_word = word.lower().strip(punctuation)
#     window.append(cleaned_word)
#     if len(window) == 2:
#       if window[0] in successor_map:
#         successor_map[window[0]].append(window[1])
#       else:
#         successor_map[window[0]] = [window[1]]
#       window.pop(0) 

for line in reader:
    for word in line.split():
        cleaned_word = word.lower().strip(punctuation)
        window.append(cleaned_word)
        if len(window) == 3:
            key = (window[0], window[1])  # Use a tuple of two words as the key
            if key in successor_map:
                successor_map[key].append(window[2])
            else:
                successor_map[key] = [window[2]]
            window.pop(0)

reader.close()  # Close the file after reading

# print(successor_map['from'])

# word = 'with'
# for i in range(15):
#   print(word, end=' ') # this prints the words on a single line
#   word = random.choice(successor_map[word])
# random.seed(1)
word1 = "the"
word2 = "concept"

for i in range(1000):
  print (word1, end=" ")
  successors = successor_map.get((word1, word2), [""])
  word3 = random.choice(successors)
  word1 = word2
  word2 = word3




