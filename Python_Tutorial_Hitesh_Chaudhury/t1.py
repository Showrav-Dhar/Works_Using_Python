def truth_table(p, q):
    props = {"p": p, "q": q, "~p": not p, "~q": not q}  # dictionary

    props["p ∨ q"] = props["p"] or props["q"]
    props["p ∧ q"] = props["p"] and props["q"]
    props["p → q"] = not props["p"] or props["q"]  # Implication rule
    props["p ↔ q"] = (props["p"] and props["q"]) or (not props["p"] and not props["q"])  # Bi-conditional rule

    table = [[]]  # list of list

    # Add each row with formatted values
    table.extend([[str(value) for value in props.values()]] for _ in range(1))

    return table


# application
print("[  'p',    'q',    '~p',    '~q',   'p ∨ q', 'p ∧ q', 'p → q', 'p ↔ q']")
props_table = truth_table(True, True)
for row in range(1,len(props_table)):
    print(props_table[row])

props_table = truth_table(True, False)
for row in range(1,len(props_table)):
    print(props_table[row])

props_table = truth_table(False, True)
for row in range(1,len(props_table)):
    print(props_table[row])

props_table = truth_table(False, False)
for row in range(1,len(props_table)):
    print(props_table[row])
