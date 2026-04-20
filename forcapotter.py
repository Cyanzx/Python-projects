import random

print("1 - ANIMAIS")
print("2 - PLANTAS")
print("3 - PERSONAGENS")
print("4 - TIMES DE QUADRIBOL")
print(" - ALEATORIO")

try:
    categoria = int(input("Qual categoria você gostaria de escolher(NUMERO): "))
except ValueError:
    print("INSIRA O NUMERO DA OPÇÃO!")
    exit()


dic_personagens = {
    "Harry Potter" : "verde",
    "Hermione Granger" : "livro",
    "Ron Wesley": "comida",
    "Albus Dumbledore": "Fênix",
    "Severus Snape": "Preto",
    "Draco Malfoy": "Pavão",
    "Rubeus Hagrid": "Aranha",
    "Sirius Black": "Nobre",
    "Remus Lupin": "",
    "Minerva McGonagall": "gato",
    "Lord Voldemort": "",
    "Bellatrix Lestrange": "",
    "Neville Longbottom": "esqueci!",
    "Luna Lovegood": "",
    "Ginny Weasley": "Harpias de Holyhead",
    "Fred Weasley": "Jred",
    "George Weasley": "Forge",
    "Percy Weasley": "Monitor",
    "Molly Weasley": "",
    "Arthur Weasley": "Patinho de borracha",
    "Dobby": "Roupa",
    "Lucius Malfoy": "",
    "Narcissa Malfoy": "",
    "Peter Pettigrew": "queijo",
    "Dolores Umbridge": "Rosa",
    "Cho Chang": "",
    "Cedric Diggory": "Banheiro dos monitores",
    "Fleur Delacour": "Gabrielly",
    "Viktor Krum": "Quadribol",
    "Nimphadora Tonks": "Arcoiris",
}

dic_personagens = { k.lower(): v.lower() for k, v in dic_personagens.items() }
#para keys.lower e v.lower em dicionarios . itens

dic_plantas = {
    "Mandragora": "Grita!",
    "Visgo do Diabo": "No sol definha",
    "Salgueiro Lutador": "",
    "Tentacula Venenosa": "",
    "Erva-de-Sapo": "",
    "Fluxweed": "",
    "Asfodelo": "",
    "Artemisia": "",
    "Raiz de Valeriana": "",
    "Bulbo Saltitante": "",
    "Gerânio Dentado": "",
    "Gillyweed": "",
    "Shrivelfig": "",
    "Salgueiro Branco": "",
    "Rosa Selvagem": "",
    "Urtiga": "",
    "Erva Mágica": "",
    "Planta Mimbulus Mimbletonia": "",
    "Abóbora Gigante": "",
    "Figo Encantado": "",
}

dic_plantas = {p.lower(): l.lower() for p,l in dic_plantas.items()}

dic_animais = {
    "Hipogrifo": "",
    "Basilisco": "",
    "Fênix": "",
    "Dementador": "",
    "Acromântula": "",
    "Testrálio": "Não te vejo.",
    "Unicórnio": "",
    "Dragão": "Bafo de fogo",
    "Trasgo": "fedor",
    "Elfo Doméstico": "",
    "Centauro": "",
    "Sereiano": "",
    "Grifo": "",
    "Duende": "",
    "Niffler": "",
    "Occamy": "",
    "Bowtruckle": "",
    "Erumpente": "",
    "Graphorn": "",
    "Kappa": "",
    "Kelpie": "",
    "Lobisomem": "",
    "Pelúcio": "",
    "Porlock": "",
    "Quimera": "",
    "Rúnspoor": "",
    "Swooping Evil": "",
    "Troll da Montanha": "",
    "Yeti": "",
    "Zumbi": "",
}

dic_animais = {a.lower(): n.lower() for a,n in dic_animais.items()}

def categoria_selecionada():
    if categoria == 1:
        escolha_animais = random.sample(dic_animais.keys(), 1)[0]
        print(escolha_animais)

    elif categoria == 2:
        pass
    elif categoria == 3:
        pass
    elif categoria == 4:
        pass
    else:
        print(" A CATEGORIA SELECIONADA NÃO EXISTE!")

