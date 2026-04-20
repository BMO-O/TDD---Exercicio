DIRECOES = {
    'w': (-1, 0), #Cima, row -1 e col não muda
    's': (1, 0), #Baixo, row +1 e col não muda
}

class Snake:
    
    def __init__(self, pos_inicial: tuple, direcao: str):
        self.corpo = [pos_inicial]
        self.direcao = direcao

    def mover(self):
        dr, dc = DIRECOES[self.direcao]
        row, col = self.corpo[0]
        self.corpo[0] = (row + dr, col + dc)
