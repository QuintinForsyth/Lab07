
## use print(ss[::-1])
def substr(word,index,length):
  """
  prints special
  """
  new_word = ("")
  for i in range(index,length):
    try:
      new_word = new_word + word[i]
    except:
      return new_word

def get_word():
  """
  gets word
  """
  word = input("Enter a word: ")
  return word

def get_length():
  """
  gets length
  """
  try: 
    len = int(input("Enter a length: "))
    return len
  except ValueError:
    print ("Please enter a integer")
    get_length()
  
def get_index():
  """
  gets index
  """
  try: 
    ind = int(input("Enter a index: "))
    return ind
  except ValueError:
    print ("Please enter a integer")
    get_index()

word = get_word()
index = get_index()
length = get_length()

word = substr(word, index, length)
print(word)