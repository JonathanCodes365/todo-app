import json
with open("tasks.json", "r") as file:
    tasks=json.loads(file.read())

print(tasks)
print(type(tasks))


def addtasks(task):
    tasks.append(task)



def viewtasks():
    if not tasks:
        print("List is empty")
    for number, task in enumerate(tasks):
        print(f"{number+1}. {task}")


def delete_tasks():
    #we have used delete_Tasks to actually delete the task.
    if tasks:
        while True:
            try:
                viewtasks()
                try:
                    delete = int(input("Enter the element's position you want to delete"))
                except ValueError:
                    print("Please! Strictly use numericals like 1 , 2 ,3 ,4 ")
                    continue
                del tasks[delete-1]
                break
            except IndexError:
                print("You have entered a wrong number for the data.")

def complete_tasks():
    while True:
        try:
            try:
                x = int(input("Enter the task you want to mark as completed"))
            except ValueError:
                print("Please:Enter the number of the task you want to modify...")
                continue
            x = x-1
            if "[✓]" in tasks[x]:
                print("You have already marked this task as completed. Please Choose Another.Thankyou")
                continue
            tasks[x] = tasks[x]+"[✓]"
            viewtasks()
            break
        except IndexError:
            print("You have selected a wrong number to modify.")


def menu():
    while True:

        print("=====Welcome to MY TODO APP =====")
        print("1.Add Task")
        print("2.View Task")
        print("3.Delete Task")
        print("4.Modify Task")
        print("5.Exit")

        try:    
            choice = int(input("Enter the number for your desired task😭😭"))
            return choice
        except ValueError:
            print("Invalid Value/data type  :Please Enter 1, 2, 3,4 or 5")
    


choice = menu()

while True:
    if choice == 1:
        task = input("Enter the tasks")
        addtasks(task)
    elif choice ==2:
        viewtasks()

    #Deletion Loop:
    elif choice ==3:
        delete_tasks()
        viewtasks()

    #completed  logic:
    elif choice ==4:
        viewtasks()
        complete_tasks()

    elif choice ==5:
        with open("tasks.json", "w") as file:
            data = json.dumps(tasks)
            file.write(data)
            break
    else:
        print("Please,Enter a valid number either 1/2/3/4/5")
    choice = menu()
print("Goodbye!!")


