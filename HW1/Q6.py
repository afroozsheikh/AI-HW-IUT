class State:
    def __init__(self, orders):
        self.order = orders
        self.parent = None
        self.heuristic = 0


def cal_heuristic(ls):
    h = 0
    global goal
    for i in range(len(ls)):
        if goal[i] != ls[i]:
            h += 1
    return h


def find_neighbours(obj):
    ls = obj.order
    ls1 = ls[:]
    ls2 = ls[:]
    ls3 = ls[:]
    ls4 = ls[:]

    neighbours = []
    king_index = ls.index(1)
    if (king_index+1) % 4 == 1:
        try:
            ls1[king_index], ls1[king_index+1] = ls1[king_index+1], ls1[king_index]
            neighbours.append(ls1)
        except:
            pass
        try:
            ls2[king_index], ls2[king_index+3] = ls2[king_index+3], ls2[king_index]
            neighbours.append(ls2)
        except:
            pass
        try:
            ls3[king_index], ls3[king_index+4] = ls3[king_index+4], ls3[king_index]
            neighbours.append(ls3)
        except:
            pass
        try:
            if king_index >= 4:
                ls4[king_index], ls4[king_index-4] = ls4[king_index-4], ls4[king_index]
                neighbours.append(ls4)
        except:
            pass
    elif (king_index+1) % 4 == 2:
        try:
            ls1[king_index], ls1[king_index + 1] = ls1[king_index + 1], ls1[king_index]
            neighbours.append(ls1)
        except:
            pass
        try:
            if king_index >= 1:
                ls2[king_index], ls2[king_index - 1] = ls2[king_index - 1], ls2[king_index]
                neighbours.append(ls2)
        except:
            pass
        try:
            ls3[king_index], ls3[king_index + 4] = ls3[king_index + 4], ls3[king_index]
            neighbours.append(ls3)
        except:
            pass
        try:
            if king_index >= 4:
                ls4[king_index], ls4[king_index - 4] = ls4[king_index - 4], ls4[king_index]
                neighbours.append(ls4)
        except:
            pass
    elif (king_index+1) % 4 == 3:
        try:
            ls1[king_index], ls1[king_index + 1] = ls1[king_index + 1], ls1[king_index]
            neighbours.append(ls1)
        except:
            pass
        try:
            if king_index >= 1:
                ls2[king_index], ls2[king_index - 1] = ls2[king_index - 1], ls2[king_index]
                neighbours.append(ls2)
        except:
            pass
        try:
            ls3[king_index], ls3[king_index + 4] = ls3[king_index + 4], ls3[king_index]
            neighbours.append(ls3)
        except:
            pass
        try:
            if king_index >= 4:
                ls4[king_index], ls4[king_index - 4] = ls4[king_index - 4], ls4[king_index]
                neighbours.append(ls4)
        except:
            pass
    elif (king_index+1) % 4 == 0:
        try:
            if king_index >= 3:
                ls1[king_index], ls1[king_index - 3] = ls1[king_index - 3], ls1[king_index]
                neighbours.append(ls1)
        except:
            pass
        try:
            if king_index >= 1:
                ls2[king_index], ls2[king_index - 1] = ls2[king_index - 1], ls2[king_index]
                neighbours.append(ls2)
        except:
            pass
        try:
            ls3[king_index], ls3[king_index + 4] = ls3[king_index + 4], ls3[king_index]
            neighbours.append(ls3)
        except:
            pass
        try:
            if king_index >= 4:
                ls4[king_index], ls4[king_index - 4] = ls4[king_index - 4], ls4[king_index]
                neighbours.append(ls4)
        except:
            pass
    return neighbours


n = int(input())
goal = [int(x) for x in input().split()]
initial_state = [i+1 for i in range(n)]
initial_obj = State(initial_state)
goal_obj = State(goal)


frontier = set()
num_jumps = {}  # store distance from starting node
current = initial_obj
frontier.add(current)

while frontier:
    current = min(frontier, key=lambda o: o.heuristic)
    if current.order == goal:
        path = []
        while current.parent:
            path.append(current.order)
            current = current.parent
        path.append(current.order)
        break
    # Remove the item from the open set
    frontier.remove(current)

    for i in find_neighbours(current):
        i_obj = State(i)
        i_obj.heuristic = cal_heuristic(i)
        # Set the parent to our current item
        i_obj.parent = current
        # Add it to the set
        frontier.add(i_obj)


print(path)
print(len(path)-1)
