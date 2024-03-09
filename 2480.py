#dice 4

d1,d2,d3 = input().split()

if(d1==d2==d3):
    result = 10000 + int(d1) * 1000
    print(result)

elif(d1 == d2 and d1 != d3):
    result = 1000 + int(d1) * 100
    print(result)
    
elif(d1 == d3 and d1 != d2):
    result = 1000 + int(d1) * 100
    print(result)

elif(d2 == d3 and d2 != d1):
    result = 1000 + int(d2) * 100
    print(result)

elif(d1!=d2 and d1 != d3 and d2 != d3):
    max = d1
    if(max<d2):
        max = d2
    if(max < d3):
        max = d3
    print(int(max) * 100)
