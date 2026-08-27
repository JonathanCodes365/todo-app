tasks=[]

def addtasks(task):
    tasks.append(task)

def askuser():
    continuous =  input("Do you want to enter tasks (Y/N)?")
    return continuous

def viewtasks():
    for number, task in enumerate(tasks):
        print(f"{number+1}. {task}")

def deletetasks():
    delete = int(input("Enter the number you want to delete"))
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

#till now we have created the general menu section of what it must look like
#next we will create what the essential code- workflow would look like.


continuous = askuser()


#now, we want to make sure we are able to input tasks till there are 'n' number of tasks.
while continuous.capitalize() == "Y":
    task = input("Enter the tasks")
    addtasks(task)
    viewtasks()
    del tasks[deletetasks()-1]
    
    #we need to make sure we get local value of continuous again and again from function_askuser
    continuous = askuser()


print(tasks)

