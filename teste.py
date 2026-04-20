from snake import Snake

def test_mover_para_cima():
    cobra = Snake(pos_inicial=(5, 5), direcao='w')
    cobra.mover()
    assert cobra.corpo[0] == (4, 5)
