while True:
     try:
          number = input("try to enter a number : ")
          print(input(number))
          break
     except ValueError:
          print("Invalid number enter a number :")
print(number + " is a number")