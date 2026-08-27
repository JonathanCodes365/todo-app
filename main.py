tasks=[]

def addtasks(task):
    tasks.append(task)

def askuser():
    continuous =  input("Do you want to enter tasks (Y/N)?")
    return continuous

continuous = askuser()

#now, we want to make sure we are able to input tasks till there are 'n' number of tasks.
while continuous.capitalize() == "Y":
    task = input("Enter the tasks")
    addtasks(task)
    #we need to make sure we get local value of continuous again and again from function_askuser
    continuous = askuser()


print(tasks)