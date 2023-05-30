# class T:
#     def __init__(self,)
# def tree_split(T):
#     return pass

# n_nodes = input()


# n, X , C = [int(i) for i in input().split(" ")]
# x = [int(i) for i in input().split(" ")]
# y = [int(i) for i in input().split(" ")]
# max_ratio = 0
# for i in range(n):
#     ratio = y[i]/x[i]
#     if ratio > max_ratio:
#         max_ratio = ratio
#         max_ind = i

# V = x[max_ind]
# ans = y[max_ind]
# while True:
#     V = V * 2
#     if V < C:
#         ans = ans*2 + X
#     else:
#         V = V / 2
#         break
# if C-V>0:
#     ind_complement = x.index(C - V)
#     ans = ans + y[ind_complement]
# print(ans)

n = int(input())
values = [int(i) for i in input().split(" ")]
colors = list(input())
R,B = [], []
for v, c in zip(values, colors):
    if c == 'R':
        R.append(v)
    else:
        B.append(v)
m = int(input())
times = [int(i) for i in input().split(" ")]
items = [int(i) for i in input().split(" ")]

def sum(R,B):
    sum_ = 0
    for j in R:
        sum_ += j
    for j in B:
        sum_ += j
    return sum_

ans = [0]
for i, t in enumerate(times):
    while i < t:
        R = [i + 1 for i in R]
        B = [i - 1 for i in B]
        i+=1
    if items[i] == 0:
        sum_ = sum(R,B)
        ans[0] += 1
        ans.append(sum_)
    elif items[i] > 0:
        R.remove(values[items[i]-1])
    else:
        R.append(values[-items[i]-1])
print(ans)
    


