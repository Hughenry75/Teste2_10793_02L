# Importação das bibliotecas e das funções necessárias para o jogo
# tkinter para termos elementos gráficos
# Random para podermos gerar resultados aleatórios para o jogo

import tkinter as tk
from tkinter import messagebox
import random

# Esta definção da classe não era imprescindível, 
# mas entendemos que deveríamos fazer uso dos nossos conhecimentos nesse domínio

class Jogo_Futebol(tk.Tk):
    
    """
    ### Aqui está a inicialização do jogo, usando as melhores práticas:
    - Começando por inicializar a sua classe
    - Depois criando a janela
    - Depois criando os widgets 
    """
    
    def __init__(self):
        super().__init__()
        
        self.title("Jogo de Futebol")
        self.geometry("300x350")

        self.criar_widgets()

    def criar_widgets(self):
        
        """
        ### Aqui vamos chamar cada um dos widgets:
        1) Criar  o display, de forma a tornar a experiência agradável e interessante
        2) Depois usando uma novidade de ter os sliders para os níveis da equipa
        3) Finalmente, criando os botões de jogar e sair
        """
        
        self.Montar_o_display()
        self.Niveis_Equipas()
        self.Criar_botoes()

    def Montar_o_display(self):
        
        """
        ### Alguns pontos:
        - Usámos o sistema de pack e não grid para termos mais controlo sobre o posicionamento dos elementos;
        - Criámos os elementos em sequência, também para controlar melhor o seu posicionamento 
        """
        
        nomes_equipas_label = tk.Label(self, text="Introduza por favor os nomes das equipas.", font=("Arial", 10, "bold"))
        nomes_equipas_label.pack(anchor="w", padx=10, pady=(10, 5))

        nome_equipa1_label = tk.Label(self, text="Equipa 1:", font=("Arial", 8))
        nome_equipa1_label.pack(anchor="w", padx=10)
        
        self.intro_equipa1 = tk.Entry(self)
        self.intro_equipa1.pack(anchor="w", padx=10)
        
        nome_equipa2_label = tk.Label(self, text="Equipa 2:", font=("Arial", 8))
        nome_equipa2_label.pack(anchor="w", padx=10)

        self.intro_equipa2 = tk.Entry(self)
        self.intro_equipa2.pack(anchor="w", padx=10)

        nome_classificacao_label = tk.Label(self, text="Seleccione por favor o nível das equipas.", font=("Arial", 10, "bold"))
        nome_classificacao_label.pack(anchor="w", padx=10, pady=(30, 0))

    def Niveis_Equipas(self):
        
        """
        ### Usámos o "Scale" para criar os sliders, que achámos interessante para definir o nível das equipas
        """
        
        self.escalao_equipa1 = tk.Scale(self, label="Equipa 1: ", from_=0, to=10, orient=tk.HORIZONTAL)
        self.escalao_equipa1.pack(anchor="w", padx=10)

        self.escalao_equipa2 = tk.Scale(self, label="Equipa 2: ",from_=0, to=10, orient=tk.HORIZONTAL)
        self.escalao_equipa2.pack(anchor="w", padx=10)

    def Criar_botoes(self):
        
        """
        ### Os botões de jogar e sair foram criados da forma que aprendemos, associando funções como comandos
        """       
        
        jogar_button = tk.Button(self, text="JOGAR", command=self.jogar)
        jogar_button.pack(side="left", padx=10, pady=(10, 5))

        sair_button = tk.Button(self, text="SAIR", command=self.sair)
        sair_button.pack(side="right", padx=10, pady=(10, 5))

    def jogar(self):
        
        """
        ### Esta função faz o elementar, que é:
        - Com o método get atribuímos os valores das caixas aos nomes das equipas
        - Caso nada seja seleccionado, assume nomes por omissão
        - Com o método get atribuímos os valores dos sliders ao nível das equipas
        - Usamos uma função random para cada equipa que vai de zero ao seu nível (inteiro, para haver empate)
        - Em função do random, comparamos e com o "if" atribuímos um resultado ao jogo
        """        
        
        equipa1_nome = self.intro_equipa1.get()
        if not equipa1_nome:
            equipa1_nome = "Equipa 1"
        equipa2_nome = self.intro_equipa2.get()
        if not equipa2_nome:
            equipa2_nome = "Equipa 2"
        equipa1_classificacao = self.escalao_equipa1.get()
        equipa2_classificacao = self.escalao_equipa2.get()

        resultado_1 = random.randint(0, equipa1_classificacao)
        resultado_2 = random.randint(0, equipa2_classificacao)

        vencedor = equipa1_nome if resultado_1 > resultado_2 else equipa2_nome
        vencedor = "Empate" if resultado_1 == resultado_2 else vencedor

        messagebox.showinfo("Resultado", f"O vencedor é: {vencedor}")

    def sair(self):
        
        """
        ### Temos também um botão para sair de forma elegante do jogo.
        """
        
        messagebox.showinfo("Mensagem", "Agradecemos a sua participação! O programa irá encerrar.")
        self.destroy()

# Estas duas linhas definem a app como uma instância da classe Jogo_Futebol e inicializa-a.

app = Jogo_Futebol()
app.mainloop()