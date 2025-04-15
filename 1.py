VALOR_SORVETE_POR_QUILO = 33
VALOR_CALDA = 1
VALOR_RECIPIENTE_COMESTIVEL = 1.5

peso = float(input("Quantos kg tem o sorvete?"))
valorSorvete = VALOR_SORVETE_POR_QUILO * peso

recipienteComestivel = str(input("O recipiente é comestível?"))

if recipienteComestivel == "Sim":
    valorSorvete += VALOR_RECIPIENTE_COMESTIVEL


calda = str(input("Quer calda?"))

if calda == "Sim":
    valorSorvete += VALOR_CALDA

print(f"O valor final do sorvete é de {valorSorvete}")
