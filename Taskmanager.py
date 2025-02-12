def task():
    tasks= []
    print("Welcome to the task manager")

    total_task = int(input("How many task you want to add ? :"))

    for i in range(total_task):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1-Add\n 2-Update\n 3-Delete\n 4-View\n 5-Exit"))
        if operation == 1:
            add = input("Enter the new task : ")
            tasks.append(add)
            print(f"Task {add} has been added successfully added !")

        elif operation == 2:
            update = input("Enter the task you want to update : ")
            if update in tasks:
                up = input("Enter the new task : ")
                ind = tasks.index(update)
                tasks[ind] = up 
                print(f"updated task {up} !")
            else:
                print(f"Task {update} not found !")

        elif operation == 3:
            dele = input("which task you want to delete : ") 
            if dele in tasks:
                ind = tasks.index(dele)
                del tasks[ind]
                print(f"{dele} task is delete successfully !!")

            else:
                print("Enter task in not found in the list")

        elif operation == 4:
            print(f"Total tasks : {tasks}")

        elif operation == 5:
            print("Closing the progamm !!")
            break
            
        else:
            print("Enter the valid choice !!")