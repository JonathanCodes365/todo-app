tasks=[]

def addtasks(task):
    tasks.append(task)


def viewtasks():
    for number, task in enumerate(tasks):
        print(f"{number+1}. {task}")

def deletetasks():
    delete = int(input("Enter the element's position you want to delete"))
    #input gives a string
    #we must convert it to int.
    return delete


def menu():
    print("=====Welcome to MY TODO APP =====")
    print("1.Add Task")
    print("2.View Task")
    print("3.Delete Task")
    print("4.Exit")

    choice = int(input("Enter the number for your desired task😭😭"))
    return choice

choice = menu()

while choice != 4:
    if choice == 1:
        task = input("Enter the tasks")
        addtasks(task)
    elif choice == 2:
        viewtasks()
    elif choice ==3:
        del tasks[deletetasks()]
    choice = menu()
print("Goodbye!!")



#Now, what are we doing next?
# We make sure our system is robust...

# Questions like :
#1. What if someone enters 5 ?