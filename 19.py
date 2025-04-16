vel = int(input("Digite a velocidade do veiculo"))
tempo = int(input("Digite o tempo do veiculo"))

km = vel * tempo

if km > 50:
    print("Você já está na metade do caminho")

else:
    print("Ainda tem chão pra rodar")
