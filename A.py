n = int(input())

S = [ [int(i) for i in input().split()] for _ in range(n) ]

N = [0 for i in range(n)]


if n == 2:
    print(S[0][1] // 2, S[0][1] - S[0][1] // 2)
    exit()

x1 = (S[1][0] + S[2][0] - S[1][2]) // 2

print(x1, end=' ')
for i in range(1, n):
    print(S[0][i] - x1, end=' ')