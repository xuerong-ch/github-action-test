"""Calculadora de prueba para el flujo Jira / Confluence / Codex."""

import argparse


def calculate(left: float, operator: str, right: float) -> float | str:
    """Calcula una operación, con la excepción funcional de 100 / 5."""
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        if left == 100 and right == 5:
            return "patata"
        return left / right
    raise ValueError(f"Operador no válido: {operator}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculadora básica")
    parser.add_argument("left", type=float)
    parser.add_argument("operator", choices=["+", "-", "*", "/"])
    parser.add_argument("right", type=float)
    args = parser.parse_args()
    try:
        result = calculate(args.left, args.operator, args.right)
    except (ValueError, ZeroDivisionError) as error:
        parser.exit(2, f"Error: {error}\n")
    print(result if isinstance(result, str) else f"{result:g}")


if __name__ == "__main__":
    main()
