year = int(input("Enter year: \t "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap year")    
                      
    else:
        print("Leap year")
else:
    print("not leap year")

