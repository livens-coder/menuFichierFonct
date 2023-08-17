def display_tasks(todo_list):
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")

def mark_task_done(index, todo_list):
    try:
        del todo_list[index - 1]
    except IndexError:
        print("Endis sa pa ekziste nan lis la.")

def save_tasks(todo_list, file_path):
    with open(file_path, "w") as file:
        for task in todo_list:
            file.write(task + "\n")

def load_tasks(file_path):
    try:
        with open(file_path, "r") as file:
            tasks = [line.strip() for line in file]
            return tasks
    except FileNotFoundError:
        return []

def add_task(todo_list, description):
    todo_list.append(description)

file_path = r"C:/Users/ADMIN1/Desktop/PYTHON/menuFichierFonct/tasks.txt"


todo_list = load_tasks(file_path)

while True:
    print("--------------Meni------------------:")
    print("1.   Ajoute tach --------------------")
    print("2.   Afiche tach yo------------------")
    print("3.   Fini yon tach-------------------")
    print("4.   Anrejistre epi femen------------")
    print("====================================================================")

    choice = input("Chwazi yon opsyon: ")

    if choice == "1":
        description = input("Antre deskripsyon tach la: ")
        add_task(todo_list, description)
    elif choice == "2":
        display_tasks(todo_list)
    elif choice == "3":
        try:
            index = int(input("Antre nimewo tach ou vle fini: "))
            mark_task_done(index, todo_list)
        except ValueError:
            print("Nonb a dwe yon chif.")
    elif choice == "4":
        save_tasks(todo_list, "tasks.txt")
        print("Tach yo anrejistre nan fichye ki pote non 'tasks.txt'.")
        break
    else:
        print("***********Opsyon pa valab*******************.")
print("*******************************************************")
