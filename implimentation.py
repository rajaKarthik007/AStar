import numpy as np

def printArray(A):
    A = np.char.mod('%d', A)
    A = np.char.replace(A, '0', 'X', count=1)
    print(A)

def Input():
    print("Enter values in row major order:")
    inp = []
    for i in range(9):
        inp.append(int(input()))
    inp = np.reshape(np.array(inp), (3, 3))
    return inp

def H(A):
    pass

def left(A):
    

def expand(A):
    return [left(A), top(A), right(A), bottom(A)]

class node():
    def __init__(self, state, i) -> None:
        self.state = state
        self.fox = H(state) + i
        self.left = None
        self.right = None

goal = np.array([0, 1, 2 ,3, 4, 5, 6, 7, 8])
goal = np.reshape(goal, (3, 3))
state = Input()
explored = []
fringe = expand(state)




