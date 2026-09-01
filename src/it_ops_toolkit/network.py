"""Funções relacionadas a diagnósticos de rede."""


def is_valid_port(port: int) -> bool:
    """Retorna True quando a porta TCP/UDP está no intervalo válido."""
    if not isinstance(port, int):
        return False

    return 1 <= port <= 65535
