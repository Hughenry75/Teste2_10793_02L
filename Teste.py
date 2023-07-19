import unittest
from tkinter import messagebox
from app import Jogo_Futebol

class TesteJogoFutebol(unittest.TestCase):

    def test_jogar(self):
        
        app = Jogo_Futebol()

        # Dar um caso para testar (como se alguém estivesse a por os dados)
        
        app.intro_equipa1.insert(0, "Equipa A")
        app.intro_equipa2.insert(0, "Equipa B")
        app.escalao_equipa1.set(7)
        app.escalao_equipa2.set(5)

        # Chamar a função (a App foi definida com a classe)
        
        app.jogar()

        # Este método call permite ir buscar diretamente comandos da biblioteca do tkinter/Tcl, 
        
        result = app.tk.call("::tk::messageBox", "show")

        # Verifica se o vencedor faz ou não sentido
        self.assertIn("O vencedor é: ", result)

if __name__ == "__main__":
    unittest.main()

