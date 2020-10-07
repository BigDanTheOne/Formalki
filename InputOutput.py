def output(machine: dict, final_states: set):
    print("Автомат:")
    for start, transitions in machine.items():
        for end, lit in transitions:
            print(f"{start} {end} \"{lit}\"")
    print("Конечные состояния:")
    print(*final_states, sep=", ")


def input():
    n = int(input())  # количество состояний
    m = int(input())  # количество переходов
    alphabet = input().split()  # алфавит
    automate = [[] for i in range(n)]
    for i in range(m):
        begin, end, lit = input().split()
        automate[int(begin)].append((int(end), lit))
    final_states = set(input().split())  # конечные состояния
    return alphabet, automate, final_states