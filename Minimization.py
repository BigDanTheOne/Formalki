from Determination import determine
from MakingComplite import makeComplete
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
