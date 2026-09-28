#conversor de moeda
dolar: float = 5.22

while True:

  real = float(input("Insira quantidade de reais: "))
  if real == 0:
    print("Programa finalizado!")
    break
  else:
    conversao = real / dolar
    print(f"{conversao:.2}")
