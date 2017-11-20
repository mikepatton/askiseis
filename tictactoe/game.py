
def draw_board(positions):
    return """
   |   |
 {} | {} | {}
   |   |
-----------
   |   |
 {} | {} | {}
   |   |
-----------
   |   |
 {} | {} | {}
   |   |   """.format(*positions)


def board(x, o):
    if max(x + o) > 9 or min(x + o) < 1 or len(set(x) & set(o)) > 0 or abs(len(x) - len(o)) > 1 or len(x) > 5 or len(o) > 5:
        raise ValueError('Invalid Position')
    position = []
    for i in range(1, 10):
        if i in x:
            position.append('X')
        elif i in o:
            position.append('O')
        else:
            position.append(' ')
    return draw_board(position)
