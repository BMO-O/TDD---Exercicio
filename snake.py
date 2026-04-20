DIRECOES = {
    'w': (-1, 0), #Cima, row -1 e col não muda
    's': (1, 0), #Baixo, row +1 e col não muda
    'a': (0, -1), #Esquerda, row não muda e col -1
    'd': (0, 1), #Direita, row não muda e col +1
}

OPOSTOS = {
    'w': 's',
    's': 'w',
    'a': 'd',
    'd': 'a',
}
class Snake:
    
    def __init__(self, pos_inicial: tuple, direcao: str):
        self.corpo = [pos_inicial]
        self.direcao = direcao

     def mudar_direcao(self, nova: str):
        if nova != OPOSTOS[self.direcao]:
            self.direcao = nova

    def mover(self):
        dr, dc = DIRECOES[self.direcao]
        row, col = self.corpo[0]
        self.corpo[0] = (row + dr, col + dc)
