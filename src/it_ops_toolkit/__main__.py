"""Interface de linha de comando do IT Ops Toolkit."""

import argparse

from it_ops_toolkit.network import check_tcp_port


def build_parser() -> argparse.ArgumentParser:
    """Cria e configura os comandos disponíveis no toolkit."""
    parser = argparse.ArgumentParser(
        prog="it-ops-toolkit",
        description="Ferramentas de diagnóstico para operações de TI.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    check_port_parser = subparsers.add_parser(
        "check-port",
        help="Verifica se uma porta TCP está acessível.",
    )
    check_port_parser.add_argument("host", help="Hostname ou endereço IP do destino.")
    check_port_parser.add_argument("port", type=int, help="Porta TCP a verificar.")
    check_port_parser.add_argument(
        "--timeout",
        type=float,
        default=3.0,
        help="Tempo máximo de espera em segundos. Padrão: 3.",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    """Executa o comando solicitado e retorna seu código de saída."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "check-port":
        is_open = check_tcp_port(args.host, args.port, args.timeout)
        status = "ABERTA" if is_open else "FECHADA ou INACESSÍVEL"
        print(f"{args.host}:{args.port} -> {status}")
        return 0 if is_open else 1

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
