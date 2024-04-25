while True:
  animal = input("Enter your pet name: ")
  year = int(input("Enter your pet age: "))

  if animal == "dog":
    if year < 2:
        print("Puppy Food")
    else:
        print("please visit any dog care centre")
  elif animal == "cat":
    if year > 5:
        print("Senior cat food")
    else:
        print("Please visit any cat care centre")
  else:
    print("invalid, this is only for dog and cat")