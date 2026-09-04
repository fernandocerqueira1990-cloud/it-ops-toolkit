"""Testes da interface de linha de comando."""

from unittest.mock import patch

from it_ops_toolkit.__main__ import main


@patch("it_ops_toolkit.__main__.check_tcp_port", return_value=True)
def test_check_port_returns_zero_when_port_is_open(mock_check, capsys) -> None:
    """O comando deve retornar 0 e informar porta aberta."""
    result = main(["check-port", "example.com", "443"])

    assert result == 0
    assert capsys.readouterr().out == "example.com:443 -> ABERTA\n"
    mock_check.assert_called_once_with("example.com", 443, 3.0)


@patch("it_ops_toolkit.__main__.check_tcp_port", return_value=False)
def test_check_port_returns_one_when_port_is_inaccessible(mock_check, capsys) -> None:
    """O comando deve retornar 1 quando não consegue acessar a porta."""
    result = main(["check-port", "example.com", "443"])

    assert result == 1
    assert capsys.readouterr().out == "example.com:443 -> FECHADA ou INACESSÍVEL\n"
    mock_check.assert_called_once_with("example.com", 443, 3.0)
