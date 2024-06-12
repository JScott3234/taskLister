user_name = ""
tasks = ["Sample 1", "Sample 2"]
choice = None


def menu():
    print("What would you like to do? \n" + "-add task : a \n"+ "-remove task : r \n"+ "-view tasks : v \n"+ "-exit : e \n")
    choice = str(input())
    if choice == "a" :
        choice = None
        add()
    elif choice == "r" :
        choice = None
        remove()
    elif choice == "v" :
        choice = None
        view()
    elif choice == "e" :
        choice = None
        print("See ya!")
        exit
    else :
        choice = None
        print("Not a Valid Option")
        menu()

# needs a back option
def add():
    print("What will you add?")
    new_task = str(input())
    tasks.append(new_task)
    new_task = None
    print("New task Added!")
    menu()

# needs a back option
# needs index fail catches
def remove():
    print("What will you remove? *Use the List Index Number*")
    index = int(input()) - 1
    removal = str(tasks[index])
    tasks.pop(index)
    index = None
    print(removal + " has been removed.")
    removal = None
    menu()

# Add a thing to describe an empty list
# Needs index fail catches
def view():
    for i in range(0, len(tasks)):
        print(f"{i + 1} - {tasks[i]}")
    menu()

if user_name == "" :
    print("Hello! What's your name?")
    user_name = str(input())
    print(user_name + ", that's a cool name! \n" + "Let's get to organizing your work!")
    menu()
else :
    print("Let's pick up where we left off " + user_name + "!")
    menu()

# I have future plans to work on memory capabilities, I plan to make an xml
# to store the name and tasks for later runs of the program
    