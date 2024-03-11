<<<<<<< HEAD
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
=======
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
>>>>>>> 950c9b949e9a4ae6335e1ff22fc6cd0bdd0eb9cb
