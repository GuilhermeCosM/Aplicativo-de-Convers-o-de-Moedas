import requests
import tkinter as tk
from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar R${self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro R${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R${self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Yuan Chinês R${self.pegar_cotacao('CNY')}"
        self.root.ids["moeda5"].text = f"Peso Argentino R${self.pegar_cotacao('ARS')}"
        self.root.ids["moeda6"].text = f"Dólar Canadense R${self.pegar_cotacao('CAD')}"
        self.root.ids["moeda7"].text = f"Libra Esterlina R${self.pegar_cotacao('GBP')}"
    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


class JanelaLogin:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.geometry("500x300")

        texto = tk.Label(self.janela, text="Fazer login")

        email_label = tk.Label(self.janela, text="E-mail")
        email_entry = tk.Entry(self.janela)
        
        senha_label = tk.Label(self.janela, text="Senha")
        senha_entry = tk.Entry(self.janela, show="*")
        
        botao = tk.Button(
            self.janela, text="Login", command=self.clique, bg="dark green", fg="white"
        )  # Definindo a cor de fundo para dark green e a cor do texto para branco
        
        texto.pack(padx=10, pady=10)
        email_label.pack(padx=10, pady=5)
        email_entry.pack(padx=10, pady=5)
        senha_label.pack(padx=10, pady=5)
        senha_entry.pack(padx=10, pady=5)
        botao.pack(padx=10, pady=10)

    def clique(self):
        print("Fazer Login")
        self.janela.destroy()  # Fechar a janela de login

if __name__ == "__main__":
    login = JanelaLogin()
    login.janela.mainloop() 
    MeuAplicativo().run()
