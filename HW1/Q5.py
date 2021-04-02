from operator import xor, or_
from math import exp
import random
from copy import deepcopy

clauses = []
max_now = -1


def cal_clause_val(c=[], x=[]):
    c_value = deepcopy(c)
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j] < 0:
                c_value[i][j] = xor(x[(-1 * c[i][j])-1], 1)
            else:
                c_value[i][j] = x[c[i][j] - 1]

    return c_value


min_temp = 0.01
max_temp = 0.3
temperature = max_temp
cou = 0

n, m = [int(x) for x in input().split()]
cl = []
ls = []
# ## initial truth assignment
X = [0 for x in range(n)]

decay_rate = 1/n

for i in range(m):
    ls.append(input())

for i in ls:
    cl.append([int(x) for x in i.split()])

for i in cl:
    clauses.append([x for x in i if x != 0])

curr = X[:]
while True:
    temperature = max_temp * exp(-cou * decay_rate)  # this line decreases temp gradually
    if temperature < min_temp:
        break
    for i in range(n):  # for each variable
        temp = cal_clause_val(clauses, curr)
        # # calculating cost and cost_prime
        cost = 0
        for q in temp:
            or_res = 0
            for j in q:
                or_res = or_(j, or_res)
            if or_res == 1:
                cost += 1

        cost_prime = 0
        curr_temp = curr[:]
        curr_temp[i] = xor(curr[i], 1)
        clauses_val_new = cal_clause_val(clauses, curr_temp)
        for s in clauses_val_new:
            or_res = 0
            for t in s:
                or_res = or_(t, or_res)
            if or_res == 1:
                cost_prime += 1

        delta = cost_prime - cost

        p = 1 / (1 + exp(-delta / temperature))
        rand_num = random.random()
        if rand_num < p:  # go to that neighbour with probability p
            curr[i] = xor(curr[i], 1)
            cost = 0
            for q in clauses_val_new:
                or_res = 0
                for j in q:
                    or_res = or_(j, or_res)
                if or_res == 1:
                    cost += 1

            cost_prime = 0
            clauses_val_new_2 = cal_clause_val(clauses, X)
            for s in clauses_val_new_2:
                or_res = 0
                for t in s:
                    or_res = or_(t, or_res)
                if or_res == 1:
                    cost_prime += 1

            delta = cost - cost_prime
            if delta > 0:
                X[i] = curr[i]

        # -------max
        if cost > max_now:
            max_now = cost
        elif cost_prime > max_now:
            max_now = cost_prime

    cou += 1

print(max_now)
print(''.join([str(i) for i in X]))




