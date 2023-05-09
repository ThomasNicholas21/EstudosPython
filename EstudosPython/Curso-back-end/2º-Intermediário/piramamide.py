piramide = []

for i in range(1, 7):
    piramide.append('*' * i)
    print(''.join(piramide))

for i in range(1, 6):
    piramide.pop()
    print(''.join(piramide))



 