import json
with open("tasks.json", "r") as file:
    tasks=json.loads(file.read())

#we want to make sure our function save_Tasks actually 
#1. opens the file
#2. dumps the python object and converts to string 
#so data type of data is str.
def save_tasks():
    with open("tasks.json","w") as file:
     data = json.dumps(tasks)
     file.write(data)


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
                viewtasks()
                try:
                    delete = int(input("Enter the element's position you want to delete"))
                    if delete < 1 or delete > len(tasks):
                        print ('Please , Enter a proper position value')
                    else:
                        del tasks[delete-1]
                        break
                except ValueError:
                    print("Please! Strictly use numericals like 1 , 2 ,3 ,4 ")
                    continue



            #except IndexError: -->We dont need this naymore because we are using range for deletion.
                #print("You have entered a wrong number for the data.")

def complete_tasks():
    while True:
        #try: -- > dont need this try except block because : we are using range to determine the range of our operation.
            try:
                x = int(input("Enter the task you want to mark as completed"))
                if x < 1 or x > len(tasks):
                    print("Please: Select an appropriate task.")
                    continue
                x = x-1
                if "[✓]" in tasks[x]:
                    print("You have already marked this task as completed. Please Choose Another.Thankyou")
                    continue
                else:
                    tasks[x] = tasks[x]+"[✓]"
                    
                    viewtasks()
                    break
            except ValueError:
                print("Please:Enter the number of the task you want to modify...")
                continue


        #except IndexError: --> dont need this dude to the range being stated at LO 52.
            #print("You have selected a wrong number to modify.")


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
        save_tasks()
    elif choice ==2:
        viewtasks()

    #Deletion Loop:
    elif choice ==3:
        delete_tasks()
        viewtasks()
        save_tasks()

    #completed  logic:
    elif choice ==4:
        viewtasks()
        complete_tasks()
        save_tasks()

    elif choice ==5:
             break
    else:
        print("Please,Enter a valid number either 1/2/3/4/5")
    choice = menu()
print("Goodbye!!")
