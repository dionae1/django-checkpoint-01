import re


def somente_digitos(valor: str | None) -> str:
    if not valor:
        return ""

    return re.sub(r"\D", "", valor)


def formatar_celular_brasileiro(valor: str | None) -> str:
    digitos = somente_digitos(valor)

    if len(digitos) == 11:
        return f"({digitos[:2]}) {digitos[2:7]}-{digitos[7:]}"

    if len(digitos) == 10:
        return f"({digitos[:2]}) {digitos[2:6]}-{digitos[6:]}"

    return valor or ""