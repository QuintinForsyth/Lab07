
#used this to test part 3s code.
numbers = "1234"
for i in range(len(numbers)):
  line = ""
  count = -1
  for j in range(len(numbers)):
    try:
      line = line +numbers[i+j]+"\t"
    except:
      count = count+1
      line = line +numbers[count]+"\t"
  print(line)


