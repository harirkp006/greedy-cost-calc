t=int(input())
for _ in range(t):
    N,K = map(int,input().split())
    total=0
    for _ in range(N):
        Ti,Di=map(int,input().split())
        free_unit=min(K,Ti)
        charged=Ti-free_unit
        total+=charged*Di
        K-=free_unit
print(total)
