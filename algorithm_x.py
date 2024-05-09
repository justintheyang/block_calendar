def solve_exact_cover(constraints, options):
    if not constraints:
        yield []
        return

    c = min(constraints, key=lambda c: len(constraints[c]))
    for r in list(constraints[c]):
        solution = [r]
        cols = select(constraints, options, r)
        
        for s in solve_exact_cover(constraints, options):
            yield solution + s
        
        deselect(constraints, options, r, cols)

def select(constraints, options, r):
    cols = []
    for c in options[r]:
        for r2 in constraints[c]:
            for c2 in options[r2]:
                if c2 != c:
                    constraints[c2].remove(r2)
        cols.append(constraints.pop(c))
    return cols

def deselect(constraints, options, r, cols):
    for c in reversed(options[r]):
        constraints[c] = cols.pop()
        for r2 in constraints[c]:
            for c2 in options[r2]:
                if c2 != c:
                    constraints[c2].add(r2)

# # Example usage
# constraints = {j: set() for j in range(N)}  # N is the number of cells + any other constraints
# options = {r: set() for r in range(M)}  # M is the number of possible placements

# # You'll need to fill in 'constraints' and 'options' with your specific puzzle setup
# for solution in solve_exact_cover(constraints, options):
#     print("Solution:", solution)
