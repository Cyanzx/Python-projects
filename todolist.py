print('0 - sair;' \
' 1 - adicionar item;'\
' 2 - mostrar itens;'\
' 3 - remover item;'\
' 4 - adicionar a lista de concluidos;'\
' 5 - visualizar lista concluidos;')

lista_adicionados = []
lista_concluidos = []

while True:
    option1 = int(input("Qual ação gostaria de realizar:  "))
    if option1 == 0:
        print("programa encerrado...")
        break
    elif option1 == 1:
        adicionar = input("O que gostaria de adicionar a lista: ")
        lista_adicionados.append(adicionar)
    elif option1 == 2:
        print(lista_adicionados)
    elif option1 == 3:
        remover = input("Qual item gostaria de remover: ")
        lista_adicionados.remove(remover)
    elif option1 == 4:
        mover = input("Qual item gostaria de mover para a lista de concluidos:  ")
        lista_adicionados.remove(mover)
        lista_concluidos.append(mover)
    elif option1 == 5:
        print(lista_concluidos)
    else:
        print("POR FAVOR INSIRA UM VALOR VALIDO!")
