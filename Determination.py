from collections import deque
from InputOutput import output, inputNKA

def Go(automate: list, state: str, symbol: str):
    SEPARATOR = "#"
    result = set()
    for cur_state in state.split(SEPARATOR):
        for transition in automate[int(cur_state)]:
            if transition[1] == symbol:
                result.add(transition[0])
    result = list(result)
    result.sort()
    string_result = ""
    for symbol in result:
        if len(string_result) > 0:
            string_result += SEPARATOR
        string_result += str(symbol)
    return string_result


def getNewFinalStates(new_automate, previous_final_states):
    new_final_states = set()
    for new_automate_state in new_automate.keys():
        for old_state in new_automate_state:
            if old_state in previous_final_states:
                new_final_states.add(new_automate_state)
    return new_final_states


def determine(alphabet: list, automate: list, final_states: set):
    new_automate = {}
    queue = deque(["0"])
    while len(queue) != 0:
        cur_long_state = queue.popleft()
        for symbol in alphabet:
            cur_new_node = Go(automate, cur_long_state, symbol)
            if cur_new_node == "":
                continue
            if cur_long_state not in new_automate:
                new_automate[cur_long_state] = [(cur_new_node, symbol)]
            else:
                new_automate[cur_long_state].append((cur_new_node, symbol))
            if (cur_new_node not in queue) and (cur_new_node not in new_automate):
                queue.append(cur_new_node)
    new_final_states = getNewFinalStates(new_automate, final_states)
    return new_automate, new_final_states

if __name__ == '__main__':
    alphabet, NKA, final_states = inputNKA()
    DKA, determined_final_states = determine(alphabet, NKA, final_states)
    print("ДКА:")
    output(DKA, determined_final_states)
