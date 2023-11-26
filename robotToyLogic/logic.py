# Position movement add values
movpos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def executeCommand(x, y, pos, command):
    if command == "MOVE":
        dx, dy = movpos[pos]
        x += dx
        y += dy
    elif command == "LEFT":
        pos = (pos - 1) % 4
    elif command == "RIGHT":
        pos = (pos + 1) % 4
    return x, y, pos
