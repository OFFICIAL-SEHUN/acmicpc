n,m = map(int,input().split())

list = list(map(int,input().split()))
v = 0

for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if list[i] + list[j] + list[k] > m:
                continue
            else:
                v = max(v,list[i] + list[j] + list[k])

print(v)