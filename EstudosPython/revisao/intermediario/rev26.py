#Colocando em prática modularização
#Criando um to do list simples

from rev26_package import add_task

tasks = []
add_task(tasks, "Nadar")
print(*tasks)
add_task(tasks, "nadar")
print(*tasks)