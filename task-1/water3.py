def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s == (4,4,0)

# You don't need the 'already' dictionary for this code.

def successors(s):
    x, y, z = s

    # Pour from one container to another

    # Pour to x
    t = min(8 - x, y)
    if t > 0:
        yield ((x + t, y - t, z), t)

    # Pour to y
    t = min(5 - y, x)
    if t > 0:
        yield ((x - t, y + t, z), t)

    # Pour to z
    t = min(3 - z, x)
    if t > 0:
        yield ((x - t, y, z + t), t)

    t = min(8 - x, z)
    if t > 0:
        yield ((x + t, y, z - t), t)

    t = min(5 - y, z)
    if t > 0:
        yield ((x, y + t, z - t), t)

    t = min(3 - z, y)
    if t > 0:
        yield ((x, y - t, z + t), t)
