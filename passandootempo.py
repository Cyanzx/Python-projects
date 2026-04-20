import random

piadas = ("O que a o pintinho falou para o outro? Piu!","Toque toque! quem é? eu! Eu quem? Quem sou eu!" )
    
print("O meu nome é DUM-E")

    
user = input("Qual seu nome? ")
user = user.strip()
user = user.title()

while True:


    print(f" Prazer em conhecer {user}")

    comando_1 = input("O que você deseja fazer? ")

    if comando_1 == 'CANCELAR':
        break

    if comando_1 == "conta":
        conta = input("Qual tipo de conta você gostaria de fazer? ")
        if conta == "somar":
            somar1 = int(input("Insira o primeiro valor que você gostaria de somar: "))
            somar2 = int(input("Insira o segundo valor que você gostaria de somar: "))
            valor_soma = somar1 + somar2
            print("O valor da sua soma é:", valor_soma)
        elif conta == "subtrair":
            subtrair1 = int(input("Insira o primeiro valor que você gostaria de subtrair: "))
            subtrair2 = int(input("Insira o segundo valor que você gostaria de subtrair: "))
            valor_subtracao = subtrair1 + subtrair2
            print("O valor da sua soma é:", valor_subtracao)
    elif comando_1 == "piada":
        piadaescolhida = random.choice(piadas)
        print(piadaescolhida)

    elif comando_1 == "tapa":
       tapa = input("Em quem você gostaria de dar um tapa?")
       print(f"{user} deu um tapa em {tapa}!")
