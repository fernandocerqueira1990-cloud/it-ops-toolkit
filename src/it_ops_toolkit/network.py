"""Funções relacionadas a diagnósticos de rede."""

import socket


def is_valid_port(port: int) -> bool:
    """Retorna True quando a porta TCP/UDP está no intervalo válido."""
    if not isinstance(port, int):
        return False

    return 1 <= port <= 65535


def check_tcp_port(host: str, port: int, timeout: float = 3.0) -> bool:
    """Verifica se uma porta TCP está acessível no host informado."""
    if not isinstance(host, str) or not host.strip():
        return False

    if not is_valid_port(port):
        return False

    if not isinstance(timeout, (int, float)) or timeout <= 0:
        return False

    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False
