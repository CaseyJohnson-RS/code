n = int(input())
if n == 1:
    print(0)
    print(0)
    exit()

# n >= 2
N = sorted([int(i) for i in input().split()])

if (n % 2 == 0):

    S = 0

    for i in range(0,len(N) - 1, 2):
        S += abs(N[i] - N[i+1])
    
    print(len(N) // 2)
    print(S)

else:

    D = []

    for i in range(0, len(N) - 1):
        D.append(N[i+1] - N[i])

    D0 = [D[0]]
    D1 = [D[-1]]

    for i in range(2,len(D),2):
        D0.append(D0[-1] + D[i])
    
    for i in range(len(D) - 3, 0, -2):
        D1.append(D[i] + D1[-1])
    D1 = D1[::-1]

    ans = min(D0[-1],D1[0])

    for i in range(len(D0)-1):
        ans = min(ans, D0[i] + D1[i + 1])
    
    print(n//2)
    print(ans)