#func de adicionar
def add_task(list, task):
    task_capitalize = task.strip().capitalize()
    if task_capitalize in list:
        print(f"This task: '{task_capitalize}', is already on the list, do yo wish to put it again?")
        option = input("Yes or No:").lower().startswith('y')
        if option is True:
            list.append(task_capitalize)
    else:
        list.append(task_capitalize)

def remove_task(list, task):
    task_capitalize = task.strip().capitalize()
    if task_capitalize not in list:
        print(f"This task: '{task_capitalize}', is not in the list!")
    else:
        print(f'Deleting: {task_capitalize}')
        list.remove(task_capitalize)

def find_task(list, task):
    task_capitalize = task.strip().capitalize()
    if task_capitalize not in list:
        print(f"This task: '{task_capitalize}', is not in the list!")
    else:
        print("Finding Tasks...")
        print(f"Here is your task: {task}")