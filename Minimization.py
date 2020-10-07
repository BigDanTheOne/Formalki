from Determination import determine
from MakingComplite import makeComplete
from InputOutput import inputNKA, output
def minimize(automate, alphabet, final_states):
    classes = {}
    for state in automate.keys():
        if state in final_states:
            classes[state] = 1
        else:
            classes[state] = 0
    prev_number = 2
    altered = True
    while altered:
        altered = False
        for symbol in alphabet:
            new_classes = {}
            added = []
            new_number = 0
            for state in automate:
                processState(automate, state, classes, symbol, added, new_number, new_classes)
            if not prev_number == new_number:
                altered = True
                prev_number = new_number
            classes = new_classes
    return classes


def processState(automate, state, classes, symbol, added, new_number, new_classes):
    for to, letter in automate[state]:
        if not letter == symbol:
            continue
        class_transition = f"{classes[state]}#{classes[to]}"
        if class_transition not in added:
            added.append(class_transition)
            new_number += 1
        new_classes[state] = added.index(class_transition)


if __name__ == "__main__":
    alphabet, NKA, final_states = inputNKA()
    DKA, determined_final_states = determine(alphabet, NKA, final_states)
    print("Классы эквивалентности:")
    print(f"{minimize(makeComplete(DKA, alphabet), alphabet, determined_final_states)}")