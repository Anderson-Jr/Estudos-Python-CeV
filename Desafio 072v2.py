contagem = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
numesc = int(input("Insira o número que você deseja ler por extenso: "))
while numesc < 0 or numesc > 20:
    print("Entrada inválida. Tente novamnete!")
    numesc = int(input("Insira o número que você deseja ler por extenso: "))
print(contagem[numesc])
