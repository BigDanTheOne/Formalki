def makeComplete(automate, alphabet):
    size_of_automate = len(automate)
    new_state = str(size_of_automate)
    is_complete = True
    for state in automate.keys():
        for symbol in alphabet:
            has_transition = False
            for transition in automate[state]:
                if symbol == transition[1]:
                    has_transition = True
            if not has_transition:
                is_complete = False
                automate[state].append((new_state, symbol))
    if not is_complete:
        automate[new_state] = [(new_state, symbol) for symbol in alphabet]
    return automate