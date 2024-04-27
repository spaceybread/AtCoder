n = int(input())
#n, q = (map(int, input().split()))

A = []
B = []
sol = ""
for i in range(n):
    A.append(input())
for i in range(n):
    b = input()
    
    if b != A[i]:
        a = A[i]
        
        for j in range(n):
            if a[j] != b[j]:
                sol = [str(i + 1), str(j + 1)]
                break
    
print(" ".join(sol))

