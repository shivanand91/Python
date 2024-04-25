while True:
  age_num = int(input("Enter Your Age: "))
  print(age_num)

  if age_num < 13:
    print("Child")
  elif age_num < 20:
    print("Teenager")
  elif age_num < 60:
    print("Adult")
  else:
    print("Senior")      