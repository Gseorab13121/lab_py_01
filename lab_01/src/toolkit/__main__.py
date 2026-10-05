import sys

from .calculator import to_reverse_polish_notation


def main():
    # sys.argv[0] = путь к __main__.py
    # sys.argv[1] = 'calc' (команда)
    # sys.argv[2] = выражение
    if len(sys.argv) < 3 or sys.argv[1] != "calc":
        print("Использование: python -m toolkit calc \"ВЫРАЖЕНИЕ\"")
        print('Пример:        python -m toolkit calc "1 + 2 + 3 + 4 * 8"')
        return

    expression = sys.argv[2]
    rpn = to_reverse_polish_notation(expression)
    print(" ".join(rpn))


if __name__ == "__main__":
    main()