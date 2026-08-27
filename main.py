tasks=[]

def addtasks(task):
    tasks.append(task)

def askuser():
    continuous =  input("Do you want to enter tasks (Y/N)?")
    return continuous

def viewtasks():
    for number, task in enumerate(tasks):
        print(f"{number+1}. {task}")

continuous = askuser()

#now, we want to make sure we are able to input tasks till there are 'n' number of tasks.
while continuous.capitalize() == "Y":
    task = input("Enter the tasks")
    addtasks(task)
    viewtasks()
    #we need to make sure we get local value of continuous again and again from function_askuser
    continuous = askuser()


print(tasks)

#Issues currently:

# currently we are doing ask-->add --> view-->ask --> add -->view --> continue .....

#but a real to do  app doesnt work like that:

#WE GIVE user the freedom to either add /view/delete/exit