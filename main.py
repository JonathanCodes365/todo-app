tasks=[]

def addtasks(task):
    tasks.append(task)


def viewtasks():
    for number, task in enumerate(tasks):
        print(f"{number+1}. {task}")

def deletetasks():

    #so you might not see the issue here:
    #lets just assume our current tasks have 1.food 2.jog 
    #lets say you choose to delete in the menu section ...
    #as a result we will be asked ... Enter the element's position you want to delete....
    #but what if we type hello?

    #our except catches it and yes its a valueError 
    #but our system ends here and it doesnt give us the prompt to again delete .... yk kind of like telling to enter again
    # which you want to delete ? 

    try:
        delete = int(input("Enter the element's position you want to delete"))
        return delete
    #input gives a string
    #we must convert it to int.
    except ValueError:
        #note: ValueError makes sure that the type of value/data entered is in the correct format.
        print("Incorrect Index: Please-Enter a present task.")
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
    elif choice ==3:
        if not tasks:
            print("The List is empty.")
        else:
            try:
                viewtasks()
                del tasks[deletetasks()-1]
            except IndexError:
                print("You have entered a wrong number for the data.")


    elif choice ==4:
        break
    else:
        print("Please,Enter a valid number either 1 /2/3 or 4")
    choice = menu()
print("Goodbye!!")


