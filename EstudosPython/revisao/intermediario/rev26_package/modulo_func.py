#func de adicionar
def add_task(list, task):
    task_capitalize = task.capitalize()
    if task_capitalize in list:
        print(f"This task: {task_capitalize}, is already on the list, do yo wish to put it again?")
        option = input("Yes or No:").lower().startswith('y')
        if option is True:
            list.append(task_capitalize)
    else:
        list.append(task_capitalize)

def remove_task():
    ...

def list_task():
    ...