#TO-DO LIST
class Operations:
    def __init__(self):  #creating an empty task list so that we can add tasks to it
        self.tasklist=[]
    def add(self):
        self.task=input("Enter your task to be added: ")
        self.tasklist.append(self.task)   #tasks are being added to the existing task list
        print("Task added successfully")

    def remove(self):
        if self.tasklist != []:
            taskremove=int(input("Enter the task number to be removed: "))   #user enters the position at which they want to remove the task
            self.tasklist.pop(taskremove-1)
        else:
            print("The To-Do List is empty!")
        print("Task removed successfully")
    def markdone(self):
        if self.tasklist != None:
            taskdone=int(input("Enter the task number to be marked done: "))
            if 0<taskdone<=len(self.tasklist):
                self.tasklist[taskdone-1]+="[Done!]"  #This will mark the task done by adding "[Done!]" at the end of whichever task number you enter
                print("Task is marked done!")
            else:
                print("Invalid task number!")
        else:
            print("The To-Do List is empty!")
   
    
class Track(Operations):    #class Track has inherited the class operations so as to use its methods and display the final list after all performed operations:
    def track(self):
        if self.tasklist != None:
            print("Your To-Do List: ", self.tasklist)
            for i, task in enumerate(self.tasklist, start=1):
                print(f"{i}. {task}")
        else:
            print("The To-Do List is empty!")
obj=Track()
while True:
    print("WELCOME TO TO-DO LIST")
    print("1.Add task to the list \n2.Remove task from the to do list \n3.Mark the task as done \n4.Display the To-Do List \n5.Exit the app")
    userin=(input("Please enter your operation:"))
    #the user inputs the operations they want to perform and we use if-else to check which operation they want to perform:
    if userin == "1":
        obj.add()
    elif userin == "2":
        obj.remove()
    elif userin == "3":
        obj.markdone()
    elif userin == "4":
        obj.track()
    elif userin == "5":
        print("Thank you for using the application!")
        break
    else:
        print("Please enter a valid choice between 1-5: ")
        




    
        
