#blackjack

n,m = map(int,input().split())
list = list(map(int,input().split()))
result = 0
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            print(list[i],list[j],list[k])
            if (list[i] + list[j] + list[k] > m):
                continue
            else:
                result = max(result,list[i] + list[j] + list[k])
                
print(result)