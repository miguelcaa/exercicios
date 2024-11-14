# Regras:
# Uma lista pode conter numeros, strings, tuplas e ate outras listas
# Ficheiros e pastas não podem ter espaços (ficheiros tudo com letra pequena)
# Apenas classes leva letra grande no nome da classe (variaveis, funções tudo letra pequena)
# Explicar cada linha do codigo com comentarios (cada um !)
# Listas = [] ; Tuplos = ()
# Podemos usar (+) para somar e concatenar strings

# 1º Modulo #


# Variáveis


s = "Tiago"
s[0] = "d"
s[2] = "o
s = "Diogo"


print(s)
# Tuplos #


tup = ("Miguel", "Gustavo") # tuplos tem parentesis normais/curvos ()
i = 0



# Listas #



# Exer 1

# Uma lista pode conter numeros (int), strings, tuplas e até outras listas
lista = [1980, "Eu sou o milior", (1, 2, 3), ["Miguel Apolinário", "Gustavo Matos"]]

# Exer 2

# Listas pode ser concastenadas/ somadas com outras listas (+)
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

lista2  = a + b + c
print(lista2)

# Exer 3

nome = "João"
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
letras.append(nome[0])# Mete na lista letras apenas a primeira letra da variavel nome ("Joao") neste caso mete ("J")
print(letras)



# Ciclo for



# Exer 1

for i in lista: # listas podem ser alteradas e adicionadas e removidas
    lista.append("hmm")
    
    print(lista) # loop infinito mas se querer parar de ser infinito é meter o break


# Exer 2

cauengue = "Afonso Augas Cauengue Moniz"

i = 0 # Aqui determina o valo9r que "i" que é 0

for habibi in cauengue:
    print(cauengue[i])
    i = i + 1 # Antes disse mos que o valor de i era 0, já aqui adicionamos + 1 valor ao "i", então vai imprimir sempre + 1 letra



#Ciclo while



while i < len(tup): # ciclo while

    print(tup[i])
    i += 1
