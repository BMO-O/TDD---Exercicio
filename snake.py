DIRECOES = {
    'w': (-1, 0), #Cima, row -1 e col não muda
    's': (1, 0), #Baixo, row +1 e col não muda
    'a': (0, -1), #Esquerda, row não muda e col -1
    'd': (0, 1), #Direita, row não muda e col +1
}

OPOSTOS = {
    'w': 's', # Cima se != Baixo
    's': 'w', # Baixo se != Cima
    'a': 'd', # Esquerda se != Direita
    'd': 'a', # Direita se != Esquerda
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
        
class Game:

    def __init__(self, dim: tuple):
        self.linhas, self.colunas = dim
        self.cobra = Snake(pos_inicial=(self.linhas//2, self.colunas//2), direcao='w')
        self.frutas = []
        self.aparecer_fruta()

    def aparecer_fruta(self):
        posicoes_livres = [(r,c) for r in range(self.linhas) for c in range(self.colunas) if (r,c) not in self.cobra.corpo]
        frutas = random.choice(posicoes_livres)
        self.frutas.append(frutas)

