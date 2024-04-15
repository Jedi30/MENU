while True:
    try:
        number = input("enter a number :")
        print(int(number))
        break
    except ValueError:    
        print("Invalid number enter a number :")

print(number + " is a number")