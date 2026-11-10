VALOR_MINIMO_PEDIDO = 30
VALOR_PARA_DESCONTO = 100
PERCENTUAL_DESCONTO = 10


def pedido_atingiu_valor_minimo(valor_pedido):
    """Regra 1 (Pedro Nunes): pedido de R$ 30,00 ou mais atinge o mínimo."""
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")
    return valor_pedido >= VALOR_MINIMO_PEDIDO


def calcular_desconto(valor_pedido):
    """Regra 2 (João Lucas Nunes): 10% de desconto a partir de R$ 100,00.

    Retorna o valor do desconto, não o valor final do pedido.
    """
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")
    if valor_pedido >= VALOR_PARA_DESCONTO:
        return valor_pedido * PERCENTUAL_DESCONTO / 100
    return 0
