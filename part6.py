lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encrypted = ""
shift = ""

def get_int(message):
  """
  gets integer
  """
  try:
    integer = int(input(message))
  except:
    print("\tinvalid input")
    integer = get_int(message)
  return integer

  
def encryption ():
  """
  Encrypts a sentence
  """
  encrypted = ""
  sentence = sentence_getter("\tType in a sentence")
  shift = get_int("\tWhat is the number you will be shifting the sentence by:")

  for letter in sentence:
    if letter in upper:
      pos = upper.find(letter)
      encrypted = encrypted +upper[(pos+shift) % len(upper)]
    elif letter in lower:
      pos = lower.find(letter)
      encrypted = encrypted +lower[(pos+shift) % len(lower)]
    else:
      encrypted = encrypted + letter
  print("\n\tYour encrypted sentence is shown below:\n\t"+encrypted)
  return encrypted,shift



  
  
def decryption (encrypted,shift):
  """
  Decrypts a sentence
  """
  decrypted = ""
  if encrypted ==  "":
    sentence = sentence_getter("\tType in your encrypted sentence: ")
    shift = get_int("\tWhat is the number the sentence was shifted by:")
  else:
    previous = get_int("\tWould you like to decrypt your previous sentence?\n\t1.Yes\n\t2.No")
    if(previous == 1):
      sentence = encrypted
    else:
      sentence = sentence_getter("\tType in your encrypted sentence: ")
      shift = get_int("\tWhat is the number the sentence was shifted by:")
    
    
  if (shift > 0):
    shift = -shift
  for letter in sentence:
    if letter in upper:
      pos = upper.find(letter)
      decrypted = decrypted +upper[(pos+shift) % len(upper)]
    elif letter in lower:
      pos = lower.find(letter)
      decrypted = decrypted +lower[(pos+shift) % len(lower)]
    else:
      decrypted = decrypted +letter
  print("\tYour decrypted sentence is shown below:\n\t"+decrypted)

def sentence_getter(message):
  sentence = input(message)
  error = False
  for letter in sentence.lower():
    if letter not in lower:
      if not letter == " ":
        print("invalid sentence")
        error = True
        break
  if error == True:
    sentence = sentence_getter(message)
    print(sentence)
  return(sentence)
  
while(True):
  place = get_int("\n\tWould you like to: \n\n\t1.Encrypt\n\t2.Decrypt\n\t3.Quit\n")
  if place == 1:
    encrypted,shift = encryption()
  elif place == 2:
    decryption(encrypted,shift)
  elif place == 3:
    exit()
