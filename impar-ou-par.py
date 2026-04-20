#par ou impar


while True:
    numero = int(input("insira um numero acima de 0 ou digite 0 para sair:"))

    if numero == 0:
        break
    elif numero % 2 == 0:
        print("O numero é par!")
    else:
        print("O numero é impar!")