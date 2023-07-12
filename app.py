
# Jogo da bola

# import tkinter as tk
# import random
# class SimuladorFutebol(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("Simulador de Equipa")

#         self.equipa = {"nome": "Minha Equipa", "jogadores": [], "saldo": 1000}

#         tk.Label(self, text=self.equipa["nome"]).pack()
#         tk.Label(self, text=f"Saldo: {self.equipa['saldo']}").pack()

#         tk.Button(self, text="Simular Jogo", command=self.simular_jogo).pack()

# def simular_jogo(self):
#     resultado = random.choice(['Vitória', 'Derrota', 'Empate'])
#     tk.Label(self, text=f"Resultado do jogo: {resultado}").pack()

# if __name__ == '__main__':
#     app = SimuladorFutebol()
#     app.mainloop()

import tkinter as tk
import tkinter.simpledialog as simpledialog
import random


class SimuladorFutebol(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de Equipa")

        self.equipa = {"nome": "Minha Equipa", "jogadores": [], "saldo": 1000000.00}

        tk.Label(self, text=self.equipa["nome"]).pack()
        tk.Label(self, text=f"Saldo: {self.equipa['saldo']}").pack()

        tk.Button(self, text="Simular Jogo", command=self.simular_jogo).pack()
        tk.Button(self, text="Preencher nome da Equipa", command=self.preencher_nome).pack()
        tk.Entry(self, width=40).pack()

    def simular_jogo(self):
        resultado = random.choice(['Vitória', 'Derrota', 'Empate'])
        tk.Label(self, text=f"Resultado do jogo: {resultado}").pack()

    def preencher_nome(self):
        nome_equipa = simpledialog.askstring("Preencher Nome da Equipa", "Digite o nome da Equipa:")
        if nome_equipa:
            self.equipa["nome"] = nome_equipa
            self.nome_label.config(text=self.equipa["nome"])



if __name__ == '__main__':
    app = SimuladorFutebol()
    app.mainloop()
print(app.equipa)