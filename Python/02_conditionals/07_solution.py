while True:
  print("please select order size small medium or large")
  order_size = input("Enter order size: ")
  extra_shot = True

  if extra_shot:
    coffee = order_size + " coffee with an extra shot"
  else:
    coffee = order_size + " coffee"
  print("Order: ", coffee)