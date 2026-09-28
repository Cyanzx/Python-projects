#conversor de moeda
dolar: float = 5.22

while True:

  real = int(input("Insira quantidade de reais: "))
  if real == 0:
    print("Programa finalizado!")
    break
  else:
    conversao = real * dolar
    print(conversao)
