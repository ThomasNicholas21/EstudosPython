#Colocando em prática modularização
#Criando um to do list simples

from rev26_package import add_task, remove_task, find_task

tasks = []
add_task(tasks, "Swim")
print(tasks)
add_task(tasks, "Study")
print(tasks)
add_task(tasks, "Play")
print(tasks)
add_task(tasks, "Work")
print(tasks)
add_task(tasks, "Hang out with Friends")
print(tasks)
remove_task(tasks, "Swim")
print(tasks)
remove_task(tasks, "play")
print(tasks)
find_task(tasks, "Work")