import os
import keyboard
import time
from snake import Game

class io_handler:

    x_size: int
    y_size: int
    game_speed = float
    last_input: str

    def __init__(self, dim, speed):
        self.x_size = dim[0]
        self.y_size = dim[1]

        self.game_speed = speed
        self.last_input = 'w'
        
        self.matrix = [[0] * self.x_size for _ in range(self.y_size)]

    def record_inputs(self):
        keyboard.add_hotkey('w', lambda: setattr(self, "last_input", 'w'))
        keyboard.add_hotkey('a', lambda: setattr(self, "last_input", 'a'))
        keyboard.add_hotkey('s', lambda: setattr(self, "last_input", 's'))
        keyboard.add_hotkey('d', lambda: setattr(self, "last_input", 'd'))
        keyboard.add_hotkey('esc', lambda: setattr(self, "last_input", 'end'))

    def display(self):
        def display_h_line(self):
            print('+', end='')
            print('--' * len(self.matrix[0]), end='')
            print('+')

        def display_content_line(line):
            print('|', end='')
            for item in line:
                if item == 1:
                    print('[]', end='')
                elif item == 2:
                    print('<>', end='')
                elif item == 3:
                    print('()', end='')
                else:
                    print('  ', end='')
            print('|')

        os.system('cls' if os.name == 'nt' else 'clear')
        display_h_line(self)
        for line in self.matrix:
            display_content_line(line)
        display_h_line(self)


def construir_matrix(io: io_handler, jogo: Game):
    # Zera a matrix
    for r in range(io.y_size):
        for c in range(io.x_size):
            io.matrix[r][c] = 0

    # Frutas
    for fruta in jogo.frutas:
        r, c = fruta
        io.matrix[r][c] = 3

    # Corpo
    for segmento in jogo.cobra.corpo[1:]:
        r, c = segmento
        io.matrix[r][c] = 1

    # Cabeça
    r, c = jogo.cobra.corpo[0]
    io.matrix[r][c] = 2


def game_loop():
    DIM = (20, 20)
    SPEED = 0.2

    jogo = Game(dim=DIM)
    io = io_handler(DIM, SPEED)
    io.record_inputs()

    while True:
        # Encerrar pelo jogador
        if io.last_input == 'end':
            print("Jogo encerrado pelo jogador.")
            break

        # Passa o input para a cobra
        jogo.cobra.mudar_direcao(io.last_input)

        # Atualiza a lógica
        jogo.atualizar()

        # Atualiza e renderiza a matrix
        construir_matrix(io, jogo)
        io.display()
        print(f"Tamanho: {len(jogo.cobra.corpo)} | Frutas: {len(jogo.frutas)} | Tecla: {io.last_input}")

        # Checa game over depois de renderizar
        if jogo.game_over:
            print("GAME OVER! Tamanho final:", len(jogo.cobra.corpo))
            break

        time.sleep(io.game_speed)


game_loop()
