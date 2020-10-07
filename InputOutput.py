def output(machine: dict, final_states: set):
    for start, transitions in machine.items():
        for end, symbol in transitions:
            print(f"{start}->{end} : {symbol}")
    print("Конечные состояния:")
    print(*final_states, sep=", ")


def inputNKA():
    n = int(input())  # количество состояний
    m = int(input())  # количество переходов
    alphabet = input().split()  # алфавит
    automate = [[] for i in range(n)]
    for i in range(m):
        begin, end, symbol = input().split()
        automate[int(begin)].append((int(end), symbol))
    final_states = set(input().split())  # конечные состояния
    return alphabet, automate, final_states