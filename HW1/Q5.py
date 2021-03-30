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
    print(f'-------------------------- temperature : {temperature} ----------------------------')
    for i in range(n):  # for each variable
        print(f'***************** i= {i} *********************')
        temp = cal_clause_val(clauses, X)
        print('clauses val is : ', temp)
        # ## calculating cost and cost_prime
        cost = 0
        for q in temp:
            or_res = 0
            for j in q:
                or_res = or_(j, or_res)
            if or_res == 1:
                cost += 1
        # if cost <= max_now:
        #     break
        print('cost is: ', cost)
        curr[i] = xor(X[i], 1)
        cost_prime = 0
        clauses_val_new = cal_clause_val(clauses, curr)
        print('clause val new is: ', clauses_val_new)
        for s in clauses_val_new:
            or_res = 0
            for t in s:
                or_res = or_(t, or_res)
            if or_res == 1:
                cost_prime += 1
        # if cost_prime <= max_now:
        #     break
        print('cost_prime is :', cost_prime)

        delta = cost_prime - cost
        if delta > 0:
            X[i] = curr[i]
            print('delta was positive and X is:', X)

        else:
            p = 1 / (1 + exp(-delta / temperature))
            rand_num = random.random()
            if rand_num < p:  # go to that neighbour with probability p
                X[i] = curr[i]
                print(f'delta was negative but rand_num{rand_num}<p{p} and X is{X}:', X)
            else:
                print('delta negative X is:', X)

        # -------max
        if cost > max_now:
            max_now = cost
        elif cost_prime > max_now:
            max_now = cost_prime

    if cost_prime == max_now:
        break

    cou += 1


print('final X:', X)
print('final max:', max_now)


