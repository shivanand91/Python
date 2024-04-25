while True:
   score = int(input("Enter your score: "))
   if score >= 101:
    print("Invalid Score")
    exit()
   if score >= 90:
    print("Grade A")
   elif score >= 80:
    print("Grade B")
   elif score >= 70:
    print("Grade C")
   elif score >= 60:
    print("Grade D")
   elif score < 60:
    print("Grade F")
   else:
    print("Invaild Number")
  