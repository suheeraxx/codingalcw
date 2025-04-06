#Exam Eligibility Test
med = input("Do you have any medical emergency or not (Y/N)?")
attendance = int(input("Enter the attendance of the student"))
if med == 'Y':
    print ("You are allowed")
else:
    if attendance>= 75:
        print ("You are allowed")
    else:
        print ("You are not allowed")