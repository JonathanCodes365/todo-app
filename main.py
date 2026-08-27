tasks=[]

def function_addtasks(task):
    tasks.append(task)

continuous =  input("Do you want to enter more tasks (Y/N)?")
if continuous.capitalize() == "Y":
    task = input("Enter the tasks")
    function_addtasks(task)
else:
    print(tasks)

print(tasks)