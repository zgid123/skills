"""Small temperature conversion command-line tool."""

import argparse


def convert(value: float, unit: str) -> float:
    if unit == "C":
        return value * 9 / 5 + 32
    if unit == "F":
        return (value - 32) * 5 / 9
    raise ValueError("unit must be C or F")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("value", type=float)
    parser.add_argument("unit", choices=("C", "F"))
    args = parser.parse_args()
    print(convert(args.value, args.unit))


if __name__ == "__main__":
    main()
