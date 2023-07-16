# Importação das bibliotecas e das funções necessárias para o jogo

import tkinter as tk
from tkinter import messagebox
import random

def jogar():
    
    """
    # Função principal do jogo
    ## Só precisa de ser invocada, não necessita de parâmetros 
    """
    
    equipa1_nome = intro_equipa1.get()
    equipa2_nome = intro_equipa2.get()
    equipa1_classificacao = escalao_equipa1.get()
    equipa2_classificacao = escalao_equipa2.get()

    resultado_1 = random.randint(0, equipa1_classificacao)
    resultado_2 = random.randint(0, equipa2_classificacao)

    if round(resultado_1,0) > round(resultado_2,0):
        vencedor = equipa1_nome
    elif round(resultado_1,0) < round(resultado_2,0):
        vencedor = equipa2_nome
    else:
        vencedor = "Empate"

    messagebox.showinfo("resultado", f"O vencedor é: {vencedor}")

# Função que é chamada pelo botão de saída do jogo

def clique_do_botao_sair():
    sair = messagebox.showinfo("Mensagem", "Agradecemos a sua participação! O programa irá encerrar.")
    Jogo_da_bola.destroy()  

# Criar janela

Jogo_da_bola = tk.Tk()
Jogo_da_bola.title("Jogo de Futebol")
Jogo_da_bola.geometry("300x200")
Jogo_da_bola.rowconfigure(10, weight=1)
Jogo_da_bola.columnconfigure(8, weight=1)


Nomes_Equipas = tk.Label(Jogo_da_bola, text="Nomes")
Nomes_Equipas.grid(row=0, column=0, sticky="nw")

# Criar widgets - equipa 1

nome_equipa1 = tk.Label(Jogo_da_bola, text="Equipa 1:")
nome_equipa1.grid(row=1, column=0, sticky="sw")
intro_equipa1 = tk.Entry(Jogo_da_bola)
intro_equipa1.grid(row=1, column=1)

# Criar widgets - equipa 2

nome_equipa2 = tk.Label(Jogo_da_bola, text="Equipa 2:")
nome_equipa2.grid(row=2, column=0, sticky="sw")
intro_equipa2 = tk.Entry(Jogo_da_bola)
intro_equipa2.grid(row=2, column=1)

# Definição dos elementos de classificação das equipas

posicao = 4

Jogo_da_bola.rowconfigure(posicao, weight=1)

nome_classificacao = tk.Label(Jogo_da_bola, text="Classe")
nome_classificacao.grid(row=posicao+1, column=0, sticky="nw")

nome_equipa1_classificacao = tk.Label(Jogo_da_bola, text="Equipa 1:")
nome_equipa1_classificacao.grid(row=posicao+2, column=0, sticky="w")
escalao_equipa1 = tk.Scale(Jogo_da_bola, from_=0, to=10, orient=tk.HORIZONTAL)
escalao_equipa1.grid(row=posicao+2, column=1, sticky="w")

nome_equipa2_classificacao = tk.Label(Jogo_da_bola, text="Equipa 2:")
nome_equipa2_classificacao.grid(row=posicao+3, column=0, sticky="w")
escalao_equipa2 = tk.Scale(Jogo_da_bola, from_=0, to=10, orient=tk.HORIZONTAL)
escalao_equipa2.grid(row=posicao+3, column=1, sticky="w")

# Usar um botão para jogar, associar um comando ao botão, que por sua vez chama a principal função, jogar.

botao_jogar = tk.Button(Jogo_da_bola, text="JOGAR", command=jogar)
botao_jogar.grid(row=posicao+5, column=5, sticky="s")

# Definição do botão de saída

sair = tk.Button(Jogo_da_bola, text="SAIR", command=clique_do_botao_sair)
sair.grid(row=posicao+5, column=8, sticky="s")

# Executar janela
Jogo_da_bola.mainloop()