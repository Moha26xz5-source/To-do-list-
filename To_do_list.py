tasks = {}
from tabulate import tabulate
while True:
    to_do = input("/ ")

    if to_do == "see":
        table = [[task, priority] for task, priority in tasks.items()]
        print(tabulate(table, headers=["Task", "Priority"], tablefmt="grid"))
        

    elif to_do == "add":
        task = input("Enter your task: ")
        priority = input("Enter priority of the task: ")

        tasks[task] = priority
        print(tasks)
    elif to_do == "delete":
        task = input("Enter the task you want to delete: ")
        if task in tasks:
            del tasks[task]
        else:
            print("Enter a valid name")