from snake import Snake

def test_mover_para_cima():
    cobra = Snake(pos_inicial=(5, 5), direcao='w')
    cobra.mover()
    assert cobra.corpo[0] == (4, 5)

def test_mover_para_baixo():
    cobra = Snake(pos_inicial=(5,5), direcao='s')
    cobra.mover()
    assert cobra.corpo[0] == (6, 5)
