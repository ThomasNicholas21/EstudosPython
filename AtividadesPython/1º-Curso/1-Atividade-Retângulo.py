""" 
 Fazer um programa para ler as medidas da base e altura de um retângulo.
 Em seguida, mostrar o valor da área, perímetro e diagonal
 deste retângulo, com quatro casas decimais, conforme exemplos.

"""
import math

base = float(input("Insira o valor da base: "))
altura = float(input("Insira o valor da altura: "))

area = base*altura
perimetro = 2*(base*altura)
diagonal = math.sqrt(base**2 + altura**2)  # Teorema de Pitagoras

print(f"A area, o perimetro e a diagonal sao, "
      f"respectivamente: {area:.3f}, {perimetro:.3f}, {diagonal:.3f}.")
