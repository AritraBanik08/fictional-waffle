import database

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cur = database.conn()
    database.create_table(cur)
    print_hi('PyCharm')
    # a = int(input("Enter a number: "))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
