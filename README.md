# todo-app
Simple to-do work/assignment tracker.


# Problem with file-management with file.read() and file.write()

currently we are doing : 
file = open("tasks.json", "r")
tasks = json.loads(file.read())
file.close()

and we are doing :
file = open("tasks.json", "w")
file.write(data)
file.close()

we are manually managing the data here.


our code works but there is a key problem here in our code.

so we are currently doing open file --> read file --> .....
but what if before we reach file.close we get an exception and the file never reaches close ? 

so we dont want that to happen.

so we are using a different approach to it .. there's nothing wrong with doing manually all of these tasks but 
we are making sure to use a safer appraoch than this .


# Therefore we use "with"
