# m = int(input("请输入数组长度:"))
# i = 0
# b = 0
# array = [0 for x in range(0, m)]
# arrstr = input("请输入数组元素:")
# for t in arrstr:
#     if t != ' ' and i < m:
#         array[i] = t
#         n = 0
#         count = 0
#         while n <= i:
#             if array[n] == array[i]:
#                 count += 1
#             n += 1
#         if count > b:
#             b = count
#         i += 1
# print(m - b)
# n = int(input())
# A = list(map(int, input().split()))
# print(A)
# print(set(A))
# for t in set(A):
#     print(t)
#     print(A.count(t))
# print(n - max([A.count(t) for t in set(A)]))
n = 4
str1 = "1 1 2 3"
print(str1.split())
print(map(int, str1.split()))
print(list(map(int, str1.split())))
