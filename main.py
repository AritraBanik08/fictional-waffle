import database


if __name__ == '__main__':
    cur = database.conn()
    database.create_table(cur)
    print("Enter 1 to add task: \nEnter 2 to view tasks: ")
    a = int(input("Enter a number: "))
    if a == 1:
        task = input("Enter task: ")
        database.add_task(cur, task)
    elif a == 2:
        tasks = database.view_tasks(cur)
        for task in tasks:
            print(task)
    else:
        print("Invalid input")
