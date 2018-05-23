from time import sleep


class Sessao():
    contador = 0
    usuarios = []
    def salvar(self, usuario):
        Sessao.contador += 1
        usuario.id = Sessao.contador
        self.usuarios.append(usuario)

    def fechar(self):
        pass

    def roll_back(self):
        self.usuarios.clear()

    def listar(self):
        return self.usuarios


class Conexao:
    def __init__(self):
        sleep(10)

    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass