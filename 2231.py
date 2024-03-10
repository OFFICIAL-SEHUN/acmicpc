#245 (245+2+4+5)는 256의 분해합
#198 (198+1+9+8)는 216의 분해합 -> 198은 216의 생성자

def Sum(n):
    #n -> int
    numstr = str(n)
    s = n
    for i in range(len(numstr)):
        s += int(numstr[i])
    return s

def Result(m):
    for i in range(m):
        if m == Sum(i):
            return i
        
    return 0

n = int(input())
print(Result(n))