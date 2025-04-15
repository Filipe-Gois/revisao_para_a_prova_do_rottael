salarioAtual = float(input("Digite o salário atual: "))

if salarioAtual < 500:
    salarioAtual *= 1.15
    print(f"O novo salário é de {salarioAtual}")

elif salarioAtual >= 500 and salarioAtual <= 1000:
    salarioAtual *= 1.10
    print(f"O novo salário é de {salarioAtual}")

else:
    salarioAtual *= 1.05
    print(f"O novo salário é de {salarioAtual}")
