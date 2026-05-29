import os

MAX = 3
Records = [] #list/array

def addRecord(n,t1,t2,t3): #adds a record
    if len(Records) >= MAX:
        print("Record hits maximum capacity.")
        return
    else:
        student = {"name":n, "g1":t1, "g2":t2, "g3":t3} #dictionary
        Records.append(student) #adds data to the list

def updRecord(n): #updates a record
    if not Records:
        print("No Records Found.")
        return

    for student in Records: #loops through each dictionary
        if student["name"] == n: #if user input and current data matches:
            while True:
                ave = (student["g1"] + student["g2"] + student["g3"]) / 3
                remarks = "Passed" if ave >= 75 else "Failed"
                print("\nRecord of", student["name"])
                print(f'{"NAME":<20} {"QUIZ 1":<6} {"QUIZ 2":<6} {"QUIZ 3":<6} {"AVERAGE":<8} REMARKS')
                print(f'{student["name"]:<20} {student["g1"]:<6} {student["g2"]:<6} {student["g3"]:<6} {ave:<8.2f} {remarks}')

                print("1. Quiz 1")
                print("2. Quiz 2")
                print("3. Quiz 3")
                print("4. Return to menu")
                choice = int(input("Choose quiz to update: "))
                if choice == 1:
                    student["g1"] = int(input("New score: "))
                    save()
                    print("Saved!")
                elif choice == 2:
                    student["g2"] = int(input("New score: "))
                    save()
                    print("Saved!")
                elif choice == 3:
                    student["g3"] = int(input("New score: "))
                    save()
                    print("Saved!")
                elif choice == 4:
                    break
                else:
                    print("Invalid Choice!")
            return
    print("Name not found!")

def deleteRecord(n): #deletes a record
    if not Records:
        print("No Records Found.")
        return

    for student in Records:                #alternative is for i in range(len(Records))
        if student["name"] == n:        #Records[i]["name"] == n then student.pop(i)
            Records.remove(student)
            print("Deleted successfully!")
            return

    print("Name not Found.")

def display(): #displays all records
    if not Records:
        print("Record sheet is empty!")
        return

    print("\nRECORDS")
    print(f'{"NO.":<4} {"NAME":<20} {"QUIZ 1":<6} {"QUIZ 2":<6} {"QUIZ 3":<6} {"AVERAGE":<8} REMARKS')

    for i, student in enumerate(Records): #loops through index and its value
        ave = (student["g1"] + student["g2"] + student["g3"]) / 3
        remarks = "Passed" if ave>=75 else "Failed"
        print(f'{i+1:<4} {student["name"]:<20} {student["g1"]:<6} {student["g2"]:<6} {student["g3"]:<6} {ave:<8.2f} {remarks}')

def save():
    with open("listmp14.csv", "w") as file:
        for rec in Records:
            file.write(f"{rec['name']},{rec['g1']},{rec['g2']},{rec['g3']}\n")

def retrieve():
    if os.path.exists("listmp14.csv"):
        with open("listmp14.csv", "r") as file:
            for line in file:
                name, g1, g2, g3 = line.strip().split(',')
                rec = {"name": name, "g1": int(g1), "g2": int(g2), "g3": int(g3)}
                Records.append(rec)

def menu(): #displays menu
    print("STUDENT RECORD\nMENU")
    print("1. Add")
    print("2. Update")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    choice = int(input("1-5: "))
    return choice

retrieve()
while True: #Equivalence to Main Function
    choice = menu()
    match choice:
        case 1:
            n = input("Enter a name: ")
            dupe = 0
            for student in Records:
                if student["name"] == n:
                    dupe = 1
            if dupe == 1:
                print("This name is a duplicate!")
            else:
                t1 = int(input("Enter first grade: "))
                t2 = int(input("Enter second grade: "))
                t3 = int(input("Enter third grade: "))
                addRecord(n,t1,t2,t3)
                print("Added to record!")
        case 2:
            n = input("Enter a name: ")
            updRecord(n)
        case 3:
            n = input("Enter a name: ")
            deleteRecord(n)
        case 4:
            display()
        case 5:
            save()
            exit()
        case _:
            print("Invalid Choice, try again!")

