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
    
def test_aparece_fruta():
    jogo = Game(dim=(10, 10))
    assert len(jogo.frutas) == 1

def test_aparece_fruta_na_cobra():
    jogo = Game(dim=(10, 10))
    for fruta in jogo.frutas:
        assert fruta not in jogo.cobra.corpo

def test_cobra_crece_ao_comer_fruta():
    cobra = Snake(pos_inicial=(5, 5), direcao='w')
    tamanho_inicial = len(cobra.corpo)
    cobra.crescer()
    assert len(cobra.corpo) == tamanho_inicial + 1

def test_cobra_comeu_e_cresceu():
    jogo = Game(dim=(10, 10))
    cabeca = jogo.cobra.corpo[0]
    fruta_pos = (cabeca[0], cabeca[1] + 1) # Coloca a fruta imediatamente a direita da cabeça
    jogo.frutas = [fruta_pos] 
    tamanho_inicial = len(jogo.cobra.corpo)
    jogo.atualizar()
    tamanho_depois = len(jogo.cobra.corpo)
    assert tamanho_depois == tamanho_inicial + 1
    assert fruta_pos not in jogo.frutas # verifica se a fruta foi comida e removida do jogo
        
