def Primeiro_exercicio():

    print("Sentas-te no opel ? \n 1 - Sim \n 2 - Não")
    sentar = int(input()) # tens de meter int, se nao pega uma string

    print("Deixas-te migalhas nas mesas ? \n 1 - Sim \n 2 - Não")
    sujar = int(input()) # tens de meter int, se nao pega uma string

    if (sujar == 1): # se tu sujas te vais limpar
        print("\nEntão vais limpar as mesas\n")


    if (sentar == 1 and sujar == 2 ) or (sentar == 2 and sujar == 1):
        print("\nFriend\n") #se tu sentas te mas não sujas te as mesas (ou vice verça) ent es friend

    elif (sentar == 2 and sujar == 2): # se tu não fizes  te nada ent és best friend
        print("\nBest Friend\n") 

    else: # se sujas te as mesas e sentas te no opel vais ter que limpar
        print("\nVais limpar\n") 

def Segundo_exercicio():
    a = 10
    b = 2
    c = 5
    d = b * c

    if (d < 10):
        print("\n" , d , "é menor a", a , "\n")


    if (d == 10):
        print("\n" , d , "é igual a", a , "\n")

    elif (d == 5):
        print("\n" , d , "não é igual a", a , "\n") 


# Primeiro_exercicio()

# Segundo_exercicio()