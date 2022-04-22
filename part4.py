def get_name():
  """
  gets name
  """
  word = input("Enter a name: ")
  return word

name = get_name()
print(name[::-1])