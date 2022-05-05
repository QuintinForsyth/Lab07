def get_name():
  """
  gets name
  """
  word = input("Enter a name: ")
  return word


name = get_name()
name_length = len(name)

for i in range(name_length):
  line = ""
  count = -1
  for j in range(name_length):
    try:
      line = line +name[i+j]+"\t"
    except:
      count = count+1
      line = line +name[count]+"\t"
  print(line)