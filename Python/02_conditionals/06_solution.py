while True:
    distance = int(input("enter distance in km: "))
    if distance <= 0:
        print("Invalid distance")
        exit()
    if distance < 3:
        print("Tranportation method walk")
    elif distance < 15:
        print("Transportation method bike")
    else:
        print("Transportation method car")