# print("Bora")

#print("Olá, mundo!!")

#nome = "Dev Python"
#idade = 35

#print(nome)
#print(idade)


#nome = input("Digite seu nome: ")
#idade = input("Digite sua idade: ")

#print(nome)
#print(idade)

# o input retorna os valores como string para conversão é preciso alterar antes do input

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

print(nome)
print(type(idade))
print(type(peso))

soma = 1 + 1 
multiplicacao = 4 * 4
divisao = 30 / 3
potencia = 7 ** 2


# condições

valor1 = 10
valor2 = 50

if valor1 > valor2:
    print(valor1, "é maior que", valor2)
else:
    print(valor2, "é maior que", valor1)


