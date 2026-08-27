tasks=[]

def addtasks(task):
    tasks.append(task)


def viewtasks():
    if not tasks:
        print("List is empty")
    for number, task in enumerate(tasks):
        print(f"{number+1}. {task}")

def deletetasks():
    while True:
        try:
            delete = int(input("Enter the element's position you want to delete"))
            return delete
        #input gives a string
        #we must convert it to int.
        except ValueError:
            #note: ValueError makes sure that the type of value/data entered is in the correct format or i mean it is acceptable.
            print("Please! Strictly use numericals like 1 , 2 ,3 ,4 ")


def delete_tasks():
    if tasks:
        while True:
            try:
                viewtasks()
                del tasks[deletetasks()-1]
                break
            except IndexError:
                print("You have entered a wrong number for the data.")





def menu():
    while True:

        print("=====Welcome to MY TODO APP =====")
        print("1.Add Task")
        print("2.View Task")
        print("3.Delete Task")
        print("4.Exit")

        try:    
            choice = int(input("Enter the number for your desired task😭😭"))
            return choice
        except ValueError:
            print("Invalid Value/data type  :Please Enter 1, 2, 3, or 4")
    


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

    elif choice ==4:
        break
    else:
        print("Please,Enter a valid number either 1 /2/3 or 4")
    choice = menu()
print("Goodbye!!")


#Here, we completed and fixed possible issues with deletion. #We also made sure deletion is properly prompted when needed.

#Next up is : We need to add another feature --> COmplete tasks.