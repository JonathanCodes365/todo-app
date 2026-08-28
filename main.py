tasks=[]

def addtasks(task):
    tasks.append(task)



def viewtasks():
    if not tasks:
        print("List is empty")
    for number, task in enumerate(tasks):
        print(f"{number+1}. {task}")

def deletetasks():
    #we have used deletetasks to get the position of the data ; the user wants to delete
    while True:
        try:
            delete = int(input("Enter the element's position you want to delete"))
            return delete
        #input gives a string
        #we must convert it to int.
        except ValueError:
            #note: ValueError makes sure that the type of value/data entered is in the correct format or i mean it is acceptable.
            print("Please! Strictly use numericals like 1 , 2 ,3 ,4 ")

#Note: deletetasks and delete_tasks have different purpose
def delete_tasks():
    #we have used delete_Tasks to actually delete the task.
    if tasks:
        while True:
            try:
                viewtasks()
                del tasks[deletetasks()-1]
                break
            except IndexError:
                print("You have entered a wrong number for the data.")

def completetasks():
    
    while True:
        try:
            y= int(input("Enter the task you want to mark as completed."))
            return y
        except ValueError:
            print("Please,Enter the number of the task you want to modify[Strictly Numbers]")

def complete_tasks():
    while True:
        try:
            x= completetasks()-1
            if "[✓]" in tasks[x]:
                print("You have already marked this task as completed. Please Choose Another.Thankyou")
                continue
            else:
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
        break
    else:
        print("Please,Enter a valid number either 1/2/3/4/5")
    choice = menu()
print("Goodbye!!")


#Ok , here we have made our Complete task facility more robust.
#Next up we will check whether we need multiple functions or not actually.

#we will also check whether these multiple loops are needed or not . 