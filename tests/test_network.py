"""Testes das funções de rede."""

from unittest.mock import patch

from it_ops_toolkit.network import check_tcp_port, is_valid_port


def test_accepts_valid_port() -> None:
    """Portas TCP/UDP dentro do intervalo devem ser aceitas."""
    assert is_valid_port(443) is True


def test_rejects_invalid_port() -> None:
    """Portas fora do intervalo e valores inválidos devem ser recusados."""
    assert is_valid_port(0) is False
    assert is_valid_port(65536) is False
    assert is_valid_port("443") is False


@patch("it_ops_toolkit.network.socket.create_connection")
def test_returns_true_when_tcp_connection_opens(mock_connection) -> None:
    """Deve retornar True quando a conexão TCP é aberta."""
    assert check_tcp_port("example.com", 443) is True
    mock_connection.assert_called_once_with(("example.com", 443), timeout=3.0)


@patch("it_ops_toolkit.network.socket.create_connection", side_effect=OSError)
def test_returns_false_when_connection_fails(mock_connection) -> None:
    """Deve retornar False quando a conexão falha."""
    assert check_tcp_port("example.com", 443) is False
    mock_connection.assert_called_once_with(("example.com", 443), timeout=3.0)


def test_rejects_invalid_connection_parameters() -> None:
    """Host, porta ou timeout inválidos não devem iniciar conexão."""
    assert check_tcp_port("", 443) is False
    assert check_tcp_port("example.com", 0) is False
    assert check_tcp_port("example.com", 443, timeout=0) is False
