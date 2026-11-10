from src.regras_localeats import pedido_atingiu_valor_minimo, calcular_desconto


# Responsável: Pedro Nunes
def test_pedido_atinge_valor_minimo():
    resultado = pedido_atingiu_valor_minimo(30)
    assert resultado is True


# Responsável: Pedro Nunes
def test_pedido_abaixo_do_valor_minimo():
    resultado = pedido_atingiu_valor_minimo(20)
    assert resultado is False


# Responsável: João Lucas Nunes
def test_pedido_de_150_recebe_desconto_de_10_por_cento():
    resultado = calcular_desconto(150)
    assert resultado == 15


# Responsável: João Lucas Nunes
def test_pedido_abaixo_de_100_nao_recebe_desconto():
    resultado = calcular_desconto(99.99)
    assert resultado == 0
