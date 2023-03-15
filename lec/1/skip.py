A = int(input())
B = int(input())

n = int(input())


if A > B:
    A,B = B,A


for i in range(A, B, n):
    print(i)
