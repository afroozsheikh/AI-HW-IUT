import numpy as np
np.seterr(divide='ignore', invalid='ignore')


def normalization(arr1):
    sum = 0
    for j in range(len(arr1)):
        sum += arr1[j]
    arr2 = arr1 / sum
    return arr2



n, m, T = [int(x) for x in input().split()]
R_t = [float(x) for x in input().split()]
transition_matrix = []
sensor_matrix = []

for i in range(n):
    transition_matrix.append([float(x) for x in input().split()])
for i in range(n):
    sensor_matrix.append([float(x) for x in input().split()])
observations = [int(x) for x in input().split()]

R_t_np = np.array(R_t)
transition_np = np.array(transition_matrix)
sensor_np = np.array(sensor_matrix)


filtering = [np.multiply(sensor_np[observations[0]-1], R_t_np)]


for t in range(1, T):
    tmp = []
    #for jj in range(n):
    for i in range(n):
        tmp.append(np.multiply(transition_np[i], filtering[t - 1][i]))

    temp = np.sum([i for i in tmp], axis=0)

    filtering.append(np.multiply(sensor_np[observations[t]-1], temp))

for k1 in range(T):
    filtering[k1] = normalization(filtering[k1])
print('filtering: ', filtering)
# ############### calculating bk 1:t
b_t_base = np.ones((1, n))
backwards = [b_t_base]
# backwards.append(np.multiply(sensor_np[observations[T-1]-1], np.multiply(b_t_base, transition_np[0]))])

for t in range(1, T):
    tmp2 = np.multiply(backwards[t-1], transition_np[0])
    tmp3 = []
    for f in range(n):
        tmp3.append(np.multiply(sensor_np[f], tmp2))

    backwards.append(np.multiply(np.sum([b for b in tmp3]), tmp2))

for k in range(1, T):
    backwards[k] = normalization(backwards[k][0])

print('backwards: ', backwards)


final_results = []
for q in range(T):
    final_results.append(np.multiply(filtering[q], backwards[T-q-1]))

for z in range(T):
    final_results[z] = normalization(final_results[z])

print(final_results)
# 0.844113 0.155887
# 0.839137 0.160863
# 0.607357 0.392643
# 0.683821 0.316179
# 0.242541 0.757459

