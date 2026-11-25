"""Calculadora de prueba para el flujo Jira / Confluence / Codex."""

import argparse


def calculate(left: float, operator: str, right: float) -> float:
    """Calcula una operación; la división queda pendiente para la tarea Jira."""
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        raise NotImplementedError("División pendiente de implementar")
    raise ValueError(f"Operador no válido: {operator}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculadora básica")
    parser.add_argument("left", type=float)
    parser.add_argument("operator", choices=["+", "-", "*", "/"])
    parser.add_argument("right", type=float)
    args = parser.parse_args()
    try:
        result = calculate(args.left, args.operator, args.right)
    except (ValueError, NotImplementedError, ZeroDivisionError) as error:
        parser.exit(2, f"Error: {error}\n")
    print(f"{result:g}")


if __name__ == "__main__":
    main()
