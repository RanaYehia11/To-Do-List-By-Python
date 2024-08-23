import json
tasks = []

#---- Add to list 
def Add_To_List():
    new_task = input("Enter Your new Task: ")
    comp_task = input("Completed: ")

    task_details = {
        "task": new_task,
        "completed": comp_task
    }
    
    # Try to read existing data from the file, if it exists
    try:
        with open('file.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError):
        data = []

    tasks = data  # Load existing tasks into the list
    tasks.append(task_details)  # Add new task

    # Save the updated tasks list to the file
    json_obj=json.dumps(tasks,indent=4)
    with open('file.json', 'w') as txtfile:
        txtfile.write(json_obj)
        

    print("Task is added successfully")
    print("=====================================")


#----- View List

def View_List():
    global tasks  
    with open('file.json', 'r') as file:
        data = json.load(file)
    tasks = data
    if not data:
        print("No tasks are here.")
        return
    else:
        for i, task in enumerate(data):
            if task["completed"]==True or task["completed"]=="true"  :
             status = "✔️" 
            else:
                status="❌"
            print(f"{i+1}. {task['task']} {status}")
    print("=====================================")




#------Mark_Task()
def Mark_Task():
    try:
        with open('file.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    global tasks
    tasks = data
    
    inCompleted_task=[]
    for i in tasks:
        if i["completed"]==False or i["completed"]=="false":
            inCompleted_task.append (i)
    if inCompleted_task !=[]:
     for i, task in enumerate(inCompleted_task):
        print(f"{i+1}. {task} ")
     no_of_task_incompleted=int(input("Enter the task number to mark as completed: "))
     inCompleted_task[no_of_task_incompleted-1]['completed']=True
     print("Updated Tasks List: \n")
     for task in tasks:
            print(f"- {task['task']} (Completed: {task['completed']})")
     with open('file.json', 'w') as file:
            json.dump(tasks, file)
    else:
        print("All tasks are completed")
    print("=====================================")

#_______________remove_task()

def remove_task():
    try:
        with open('file.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    global tasks
    tasks = data
    
    if not tasks:
        print("No tasks to remove.")
        return

    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['task']} (Completed: {task['completed']})")

    try:
        removed_task_index = int(input("Enter the number of the task you want to delete: ")) - 1
        
        removed_task = tasks.pop(removed_task_index)
        print(f"Task '{removed_task['task']}' removed successfully.")
        print("================================")
    except ValueError:
        print("Please enter a valid number.")

    with open('file.json', 'w') as file:
        json.dump(tasks, file)



print("1. Add To Task List ")
print("2. Mark task as completed ")
print("3. View Tasks ")
print("4. Remove Task ")
print("5. Quit ")
while(True):
    number=int(input("Enter a number: "))
    if number==1:
        Add_To_List()
        
    elif number==2:
         Mark_Task()
        
    elif number==3:
         View_List()
    elif number==4:
         remove_task()
    elif number==5:
        break
    else:
        print("Invalid number, Try Again")



