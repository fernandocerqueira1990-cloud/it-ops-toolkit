"""Teste das funções de rede."""

from it_ops_toolkit.network import is_valid_port


def test_accepts_valid_ort() -> None:
    """Portas TCP/UDP dentro do intervalo devem ser aceitas."""
    assert is_valid_port(443) is True

def test_rejects_invalid_port() -> None:
    """Portas fora do intervalo e valores inválidos devem ser recusados."""
    assert is_valid_port(0) is False
    assert is_valid_port(65536) is False
    assert is_valid_port("443") is False
