# Quadrado de Pearson
# Created by eduardorabe


ingrediente1 = int(input("Entre com a % do nutriente desejado encontrado no primeiro ingrediente: "))
ingrediente2 = int(input("Entre com a % do nutriente desejado encontrado no segundo ingrediente: "))
meta = int(input("Quantos % do nutriente a mistura deve conter? "))

if (ingrediente1 <= meta and ingrediente2 <= meta) or (ingrediente1 >= meta and ingrediente2 >= meta):
    print("Não é possível a formulação com os valores inseridos!")
else:
    aux1 = abs(ingrediente2 - meta)
    aux2 = abs(ingrediente1 - meta)
    total = aux1 + aux2

    quantidade_ingrediente1 = format((aux1 / total) * 100, ".2f")
    quantidade_ingrediente2 = format((aux2 / total) * 100, ".2f")

    print(f"Serão necessários {quantidade_ingrediente1}% do ingrediente 1")
    print(f"Serão necessários {quantidade_ingrediente2}% do ingrediente 2")
