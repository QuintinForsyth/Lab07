word = "word voweled"
vowels = "AEIOUaeiou"
count = 0
for i in range (len(vowels)):

  if vowels[i] in word:
    count=count+1


print("there was "+str(count)+" vowels in the word "+str(word))