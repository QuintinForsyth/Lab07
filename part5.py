import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "123456789"
symbol = "!@#$%^&*()-_=+.,<>[]{}\|"
password = ""

def get_int():
  """
  gets integer
  """
  while(True):
    try: 
      ind = int(input("Enter a integer relating to the ammount of characters you would like your random password to be with 8 being the minimum: "))
      if ind < 8:
        print("lower than 8, input a valid number")
        continue
      else:
        return ind
    except ValueError:
      print ("Please enter a integer")
      continue

def gen_pass(passlen,lower,upper,number,symbol):
  """
  generates a password
  """
  password = ""
  character = ""
  for i in range (passlen):
    overall_rand = random.randint(1, 4)
    if(overall_rand == 1):
      character = lower_gen(lower)
      
    elif(overall_rand == 2):
      character = upper_gen(upper)
      
    elif(overall_rand == 3):
      character = number_gen(number)
    
    elif(overall_rand == 4):
      character = symbol_gen(symbol)
      
    password = password + character
  return password

def lower_gen(low):
  """
  returns random low character
  """
  randy = random.randint(0, len(low)-1)
  return low[randy]
  
def upper_gen(up):
  """
  returns random upper character
  """
  randy = random.randint(0, len(up)-1)
  return up[randy]

def symbol_gen(sym):
  """
  returns random symbol character
  """
  randy = random.randint(0, len(sym)-1)
  return sym[randy]

def number_gen(num):
  """
  returns random low character
  """
  randy = random.randint(0, len(num)-1)
  return str(randy)

def check_for_all(check, password):
  """
  checks if all 4 specific string are being used
  """
  for i in check:
    if i in password:
      return True
  return False


  
passlen = get_int()

while(True):
  password = gen_pass(passlen,lower,upper,number,symbol)
  l = check_for_all(lower,password)
  u = check_for_all(upper,password)
  s = check_for_all(symbol,password)
  n = check_for_all(number,password)
  if l == True and u == True and s == True and n == True:
    break
  else:
    continue
  
  
print("your password is "+password)