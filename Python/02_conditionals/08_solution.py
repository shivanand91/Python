while True:
    
  password = input("Please enter your password: ")
  pass_len = len(password)
  
  if pass_len <= 0:
    print("invalid password")
    exit()
  elif pass_len < 6:
    print("Weak password please choose another password")
  elif pass_len < 10:
    print("Medium password please make it strong")
  else:
    print("Strong password")
