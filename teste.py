from snake import Snake

def test_mover_para_cima():
    cobra = Snake(pos_inicial=(5, 5), direcao='w')
    cobra.mover()
    assert cobra.corpo[0] == (4, 5)

def test_mover_para_baixo():
    cobra = Snake(pos_inicial=(5,5), direcao='s')
    cobra.mover()
    assert cobra.corpo[0] == (6, 5)

def test_mover_para_esquerda():
    cobra = Snake(pos_inicial=(5,5), direcao='a')
    cobra.mover()
    assert cobra.corpo[0] == (5, 4)

def test_mover_para_direita():
    cobra = Snake(pos_inicial=(5,5), direcao='d')
    cobra.mover()
    assert cobra.corpo[0] == (5, 6)
    
def test_mover_para_direcao_valida():
    cobra = Snake(pos_inicial=(5, 5), direcao='w')
    cobra.mudar_direcao('d')
    assert cobra.direcao == 'd'

def test_mover_para_direcao_invalida():
    cobra = Snake(pos_inicial=(5, 5), direcao='w')
    cobra.mudar_direcao('s')
    assert cobra.direcao == 'w'
