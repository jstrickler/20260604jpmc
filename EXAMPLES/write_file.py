states = [
    'Virginia',
    'North Carolina',
    'Washington',
    'New York',
    'Florida',
    'Ohio',
]

with open("states.txt", "w") as states_out: # "w" opens for writing, "a" for append
    for state in states:
        # states_out.write(state + "\n")  # write() does not automatically add newline
        print(state, file=states_out)  # this is why there is no writeln() or writeline()