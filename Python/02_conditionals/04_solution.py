while True:
    fruit_color = input("Enter your fruit color: ")
    print(fruit_color)

    if fruit_color == "Green":
      print("your fruit is Unripe")
    elif fruit_color == "Yellow":
      print("your fruit is Ripe")
    elif fruit_color == "Brown":
      print("your fruit is Overripe")
    else:
      print("invalid fruit color please mention anyone of this three types Green / Yellow and Brown")