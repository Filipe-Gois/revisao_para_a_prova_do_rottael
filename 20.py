import math

A = int(input("Digite o A"))
B = int(input("Digite o B"))
C = int(input("Digite o C"))

delta = B * B - 4 * A * C

X1 = (- B + math.sqrt(delta)) / (2 * A)
X2 = (- B - math.sqrt(delta)) / (2 * A)

print(f"X é igual a {X1} e {X2}")
