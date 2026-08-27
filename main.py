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
    elif choice ==2:
        viewtasks()
    elif choice ==3:
        viewtasks()
        del tasks[deletetasks()-1]
    choice = menu()
print("Goodbye!!")


#Here are some of the common errors we need to fix:

# 1. what if we go to menu --> but we choose 5 ?
# As a result, nothing happens : and the menu shows again showing 1, 2, 3, 4 

#2. what if at the menu --> instead of typing 1 , 2, 3 , and 4--> the person enters "hello"??
#we will get a valueError because : our choice is int--> and we got string instead of integer value ?

#3. lets say our list is empty at the begining .i.e. lists = []
# what if the person chooses to use Delete at this moment?

#4. Say, what if there are only 2 tasks e.g. 1. eat food 2. dance
#but what if the user wants to delete no.5?
#this gives us IndexError.

