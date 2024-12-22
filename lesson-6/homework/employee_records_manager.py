f = open("employee.txt", "w+")

while True:
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")
    print("----------------------------------------")
    choice = input("Choose a number between 1 and 6: ")
    if choice=="1":
        id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        pos = input("Enter employee position: ")
        salary = input("Enter employee salary: ")
        f.write(id + ", " + name + ", " + pos + ", " + salary + "\n")
    elif choice=="2":
        f.seek(0)
        print(f.read())
    elif choice=="3":
        id = input("Enter employee ID: ")
        f.seek(0)
        found = False
        for line in f.readlines():
            if line.split(", ")[0]==id:
                print(line)
                found = True
                break
        if not found:
            print("Employee with the given id does not exist.")
    elif choice=="4":
        id = input("Enter employee ID: ")
        name = input("Enter new employee name: ")
        pos = input("Enter new employee position: ")
        salary = input("Enter new employee salary: ")
        f.seek(0)
        lines = f.readlines()
        for i in range(len(lines)):
            if lines[i].split(", ")[0] == id:
                lines[i] = id + ", " + name + ", " + pos + ", " + salary + "\n"
                break
        f.seek(0)
        f.truncate(0)
        f.writelines(lines)
    elif choice=="5":
        id = input("Enter employee ID: ")
        f.seek(0)
        lines = f.readlines()
        # print(lines)
        for i in range(len(lines)):
            if lines[i].split(", ")[0] == id:
                lines.pop(i)
                print("deleted")
                break
        f.seek(0)
        f.truncate(0)
        f.writelines(lines)
    elif choice=="6":
        break
    else:
        print("Wrong choice. Try again!")

f.close()