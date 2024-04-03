import database


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cur = database.conn()
    database.create_table(cur)
    print_hi('PyCharm')
    a = int(input("Enter 1 to add task: /n Enter 2 to view tasks: "))
    if a == 1:
        task = input("Enter task: ")
        database.add_task(cur, task)
    elif a == 2:
        tasks = database.view_tasks(cur)
        for task in tasks:
            print(task)
    else:
        print("Invalid input")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
