import customtkinter as ctk
from PIL import Image



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("RECICLAGEM CONSCIENTE")
        self.wm_resizable(False,False)
        ctk.set_appearance_mode("light")
        self.geometry('450x650')
        self.configure(fg_color='#f0f7f0')

        imagem_original = Image.open("image.jpg") 
        self.bg_image = ctk.CTkImage(light_image=imagem_original,
                              dark_image=imagem_original,
                              size=(450, 650))

        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text='')
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.residuos = {
        "garrafa pet": "Lave e descarte no plástico.",
        "embalagem plástica": "Descarte no plástico limpo.",
        "sacola plástica": "Descarte no plástico ou reutilize.",
        "papel": "Descarte na coleta seletiva (azul).",
        "papelão": "Desmonte e descarte na coleta seletiva.",
        "jornal": "Descarte na coleta seletiva (papel).",
        "revista": "Descarte na coleta seletiva.",
        "caixa longa vida": "Lave e descarte no reciclável.",
        "lata de alumínio": "Lave e descarte no metal.",
        "lata de aço": "Lave e descarte no metal.",
        "vidro": "Descarte no vidro, bem embalado se quebrado.",
        "garrafa de vidro": "Lave e descarte no vidro.",
        "pote de vidro": "Lave e descarte no vidro.",
        "restos de comida": "Descarte no orgânico ou faça compostagem.",
        "cascas de frutas": "Compostagem ou lixo orgânico.",
        "borra de café": "Compostagem ou lixo orgânico.",
        "filtro de café": "Compostagem ou lixo orgânico.",
        "guardanapo sujo": "Lixo orgânico ou rejeito.",
        "papel higiênico": "Lixo comum (rejeito).",
        "fralda descartável": "Lixo comum (rejeito).",
        "absorvente": "Lixo comum (rejeito).",
        "bituca de cigarro": "Lixo comum (rejeito).",
        "isopor": "Verifique coleta local; geralmente reciclável.",
        "embalagem metalizada": "Lixo comum (difícil reciclagem).",
        "pilha": "Leve a pontos de coleta especiais.",
        "bateria": "Descarte em pontos específicos.",
        "celular antigo": "Leve a coleta de eletrônicos.",
        "carregador": "Descarte como lixo eletrônico.",
        "computador": "Leve a ecopontos ou recicladoras.",
        "televisão": "Descarte em pontos de lixo eletrônico.",
        "lâmpada fluorescente": "Ponto de coleta especial (contém mercúrio).",
        "lâmpada LED": "Descarte em coleta específica.",
        "óleo de cozinha": "Armazene e leve a ponto de coleta.",
        "medicamentos vencidos": "Leve a farmácias participantes.",
        "embalagem de remédio": "Separar; plástico/papel conforme material.",
        "roupas usadas": "Doe ou reutilize.",
        "calçados": "Doe ou descarte em coleta específica.",
        "madeira": "Reutilize ou descarte em local apropriado.",
        "móveis velhos": "Coleta especial ou ecoponto.",
        "entulho pequeno": "Leve a ecoponto.",
        "esponja de cozinha": "Lixo comum (difícil reciclagem).",
        "escova de dentes": "Lixo comum.",
        "caneta": "Lixo comum ou programas de reciclagem.",
        "brinquedos plásticos": "Doe ou descarte no plástico se possível.",
        "panos velhos": "Reutilize ou descarte no lixo comum.",
        "cosméticos": "Descarte conforme embalagem.",
        "embalagem de shampoo": "Lave e descarte no plástico.",
        "embalagem de limpeza": "Lave e descarte no plástico.",
        "aerossol": "Descarte no metal se vazio.",
        "alumínio (papel alumínio)": "Limpo, descarte no metal.",
        }

        

        self.label1 = ctk.CTkLabel(self, text="RECICLAGEM CONSCIENTE", )
        self.label1.pack(pady=20)

        
        self.entrada = ctk.CTkEntry(self, placeholder_text="INSIRA O ITEM QUE DESEJA DESCARTAR", width = 255, height= 40,)
        self.entrada.pack(pady=40)

        self.botao = ctk.CTkButton(self, text="VERIFICAR", command=self.tratar_entrada, fg_color="#0A8F15", hover_color="#17401B")
        self.botao.pack(pady=70)

        self.resultado_label = ctk.CTkLabel(self,text="",font=("Arial", 14))
        self.resultado_label.pack(pady=20)

         

    def tratar_entrada(self):
            item_digitado = self.entrada.get().lower().strip()

            if item_digitado in self.residuos:
                categoria = self.residuos[item_digitado]
                mensagem = f"{item_digitado.upper()}: {categoria}"
                self.resultado_label.configure(text=mensagem, text_color="green")
                print(f"Item encontrado: {item_digitado} - {categoria}")
            else:
                mensagem = f" '{item_digitado}' não encontrado no sistema de reciclagem!"
                self.resultado_label.configure(text=mensagem, text_color="red")
                print(f"Item não encontrado: {item_digitado}")

app = App()
app.mainloop()
