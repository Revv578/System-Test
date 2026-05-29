import os
import json

class Student: #Reperensents student record
    def __init__(self, name, g1, g2, g3):
        self.name = name
        self.g1   = g1
        self.g2   = g2
        self.g3   = g3

class RecordBook: #manages the student records

    FILENAME = "bscs1cd.json"

    def __init__(self, MAX=3):
        self.capacity = MAX
        self.students = []             # list of Student objects

    # ----------------------------------------------------------
    #  helpers
    # ----------------------------------------------------------

    def __find(self, name):
        """Return the Student object with the given name, or None."""
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def __is_full(self):
        return len(self.students) >= self.capacity

    def __is_empty(self):
        return len(self.students) == 0

    # ----------------------------------------------------------
    #  ADD
    # ----------------------------------------------------------

    def add(self, name):
        if self.__is_full():
            print("Record hits maximum capacity.")
            os.system("pause")
            return

        if self.__find(name):
            print("Name already exists in the record.")
            os.system("pause")
            return

        g1 = int(input("Enter first grade:  "))
        g2 = int(input("Enter second grade: "))
        g3 = int(input("Enter third grade:  "))

        self.students.append(Student(name, g1, g2, g3))
        self.students.sort(key=lambda student:student.name.lower())
        RecordBook.save(self)
        print("Added to record!")
        os.system("pause")

    # ----------------------------------------------------------
    #  UPDATE
    # ----------------------------------------------------------

    def update(self, name):
        if self.__is_empty():
            print("No Records Found.")
            os.system("pause")
            return

        student = self.__find(name)
        if not student:
            print("Name not found!")
            os.system("pause")
            return

        while True:
            clear_screen()
            ave = (student.g1 + student.g2 + student.g3) / 3
            remarks = "Passed" if ave >= 75 else "Failed"
            print("\nRecord of", student.name)
            print(f'{"NAME":<20} {"QUIZ 1":<6} {"QUIZ 2":<6} {"QUIZ 3":<6} {"AVERAGE":<8} REMARKS')
            print(f'{student.name:<20} {student.g1:<6} {student.g2:<6} {student.g3:<6} {ave:<8.2f} {remarks}')

            print("1. Quiz 1")
            print("2. Quiz 2")
            print("3. Quiz 3")
            print("4. Return to menu")
            choice = int(input("Choose quiz to update: "))
            if choice == 1:
                student.g1 = int(input("New score: "))
                print("Saved!")
            elif choice == 2:
                student.g2 = int(input("New score: "))
                print("Saved!")
            elif choice == 3:
                student.g3 = int(input("New score: "))
                print("Saved!")
            elif choice == 4:
                RecordBook.save(self)
                break
            else:
                print("Invalid Choice!")
    # ----------------------------------------------------------
    #  DELETE
    # ----------------------------------------------------------

    def delete(self, name):
        if self.__is_empty():
            print("No Records Found.")
            os.system("pause")
            return

        student = self.__find(name)
        if student:
            self.students.remove(student)
            RecordBook.save(self)
            print("Deleted successfully!")
        else:
            print("Name not found.")
        os.system("pause")

    # ----------------------------------------------------------
    #  DISPLAY
    # ----------------------------------------------------------

    def display(self):
     clear_screen()
     if self.__is_empty():
        print("Record sheet is empty!")
        os.system("pause")
        return

     print("\nRECORDS")
     print(f'{"NO.":<4} {"NAME":<20} {"QUIZ 1":<6} {"QUIZ 2":<6} {"QUIZ 3":<6} {"AVERAGE":<8} REMARKS')

     for i, student in enumerate(self.students): #loops through index and its value
        ave = (student.g1 + student.g2 + student.g3) / 3
        remarks = "Passed" if ave>=75 else "Failed"
        print(f'{i+1:<4} {student.name:<20} {student.g1:<6} {student.g2:<6} {student.g3:<6} {ave:<8.2f} {remarks}')
     os.system("pause")

    # ----------------------------------------------------------
    #  SAVE  (writes to file)
    # ----------------------------------------------------------

    def save(self):
        data = [
            {"name": s.name, "g1": s.g1, "g2": s.g2, "g3": s.g3}
            for s in self.students
        ]
        with open(self.FILENAME, "w") as file:
            json.dump(data, file, indent=4)
 
    # ----------------------------------------------------------
    #  RETRIEVE — reads JSON from file
    # ----------------------------------------------------------
 
    def retrieve(self):
        if not os.path.exists(self.FILENAME):
            return
        with open(self.FILENAME, "r") as file:
            data = json.load(file)
            for rec in data:
                self.students.append(
                    Student(rec["name"], rec["g1"], rec["g2"], rec["g3"]))


# =============================================================
#  MISC
# =============================================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("STUDENT RECORD\nMENU")
    print("1. Add")
    print("2. Update")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    return int(input("1-5: "))


# =============================================================
#  MAIN
# =============================================================

def main():
    record = RecordBook(MAX=3)
    record.retrieve()                     # load saved data on startup

    while True:
        clear_screen()
        choice = menu()

        match choice:
            case 1:
                clear_screen()
                name = input("Enter a name: ")
                record.add(name)

            case 2:
                clear_screen()
                name = input("Enter a name: ")
                record.update(name)

            case 3:
                clear_screen()
                name = input("Enter a name: ")
                record.delete(name)

            case 4:
                record.display()

            case 5:
                clear_screen()
                print("Thank you for using the program!")
                exit()

            case _:
                print("Invalid choice, try again!")


if __name__ == '__main__':
    main()