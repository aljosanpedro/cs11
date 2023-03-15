A = int(input())
B = int(input())

n = int(input())

if A > B:
    larger, smaller = A, B
else:
    smaller, larger = A, B

for i in range(smaller, larger, n):
    print(i)
