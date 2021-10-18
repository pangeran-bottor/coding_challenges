# my result sumarry: https://app.codility.com/demo/results/trainingSX9YDC-DEQ/

def solution(A, B):
    # write your code in Python 3.6
    alive = []
    for size, direction in zip(A, B):
        if len(alive) == 0:
            alive.append((size, direction))
        else:
            if direction == 0:
                while len(alive) > 0 and \
                      (alive[-1][1] == 1 and alive[-1][0] < size):
                    alive.pop()

                if len(alive) == 0 or alive[-1][1] == 0:
                    alive.append((size, direction))
            else:
                alive.append((size, direction))
    return len(alive)
