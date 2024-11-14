#* EXERCICIO 1 *# (Indexação em 0)

# Estrutura de dados estática
nome = "Miguel"
num = 2024
tup = (10, "Olá")

# Estrutura de dados dinânica

lista = ["Ola", 20]

lista.append(nome)
lista.append(nome[0])
lista.append(num)
lista.append(tup)

print(lista)
print(lista[5])

nome2 = "Diguel"
# nome2[0] = "D" # Não funciona burro, não da para alterar uma estrutura da dados estatica bot
nome2 = "Figuel"
print(nome2)

#* EXERCICIO 2 *# (IFs)

print("Quanto é que tives te no teste")

nota_teste = int(input())

print("Quanto é que tiveste na apresentação")

nota_apresentacao =  int(input())

nota_media = (nota_teste + nota_apresentacao) / 2

if nota_media >= 10 and nota_media <= 20:
    print("KACHOOOOW PASSAS TE. Tives te ", nota_media)

elif nota_media >= 0 and nota_media < 10:
    print("Sinto muito colega, porem vais jogar damas. Tives te ", nota_media)

else:
    print("Não sabes abrir um yogurt és muita burro")

#* EXERCICIO 3 *# (for)

cauengue = "Afonso Augas Cauengue Moniz"

i = 0 # Aqui determina o valo9r que "i" que é 0

for habibi in cauengue:
    print(cauengue[i])
    i = i + 1 # Antes disse mos que o valor de i era 0, já aqui adicionamos + 1 valor ao "i", então vai imprimir sempre + 1 letra

#* EXERCICIO 4 *# (While) (Ciclo enquanto)

metros_total = 0

while (metros_total < 3300):
    print("O pistolas saltou quantos metros ?")
    metros = int(input())

    metros_total = metros_total + metros

print("O pistolas saltou até ao hospital, com um salto de ", metros_total , "m")

#* EXERCICIO 5.1 *#

print("Diz aí 1 número")
num_1 = int(input())

print("Diz aí outro número")
num_2 = int(input())

if (num_1 > num_2):
    print("O numero maior é ", num_1)

elif (num_2 > num_1):
    print("O numero maior é ", num_2)

else:
    print("Os numeros são iguais")

#* EXERCICIO 5.2 *#

num = 0

while (num <= 10):
    print(num)
    num = num + 1

#* EXERCICIO 5.3 *#

nomes = ["Gustavo", "Miguel", "Afonso", "Cauengue", "Pistolas"]

for letra in nomes:
    print("Bem Vindo(a)", letra)

#* EXERCICIO 5.4 *#

print("\nDigite o seu nome")
nome = input()

print("Digite a sua idade")
idade = int(input())

print("Digite onde é que nasceu")
nascimento = input()

print("Nome:", nome , "\nIdade:", str(idade) , "\nLocal onde nasceu:", nascimento)