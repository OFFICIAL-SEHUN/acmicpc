s = int(input())
result = 666
cnt = 0
while True:
    if '666' in str(result):
        cnt+=1
    if cnt == s:
        break

    result += 1

print(result)