import random

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

    def crescer(self):
        cauda = self.corpo[-1]
        self.corpo.append(cauda)
        
class Game:

    def __init__(self, dim: tuple):
        self.linhas, self.colunas = dim
        self.cobra = Snake(pos_inicial=(self.linhas//2, self.colunas//2), direcao='w')
        self.frutas = []
        self.aparecer_fruta()

    def posicoes_livres(self) -> list:
        return [(r,c) for r in range(self.linhas) for c in range(self.colunas) if (r,c) not in self.cobra.corpo]

    def aparecer_fruta(self):
        livres = self.posicoes_livres()
        self.frutas.append(random.choice(livres))

    def saiu_do_mapa(self, posicao: tuple) -> bool:
        r, c = posicao
        return r < 0 or r >= self.linhas or c < 0 or c >= self.colunas

    def atualizar(self):
        self.cobra.mover()
        cabeca = self.cobra.corpo[0]
        if self.saiu_do_mapa(cabeca)
            self.game_over = True
            return

        if cabeca in self.frutas:
            self.frutas.remove(cabeca)
            self.cobra.crescer()
            self.aparecer_fruta()

