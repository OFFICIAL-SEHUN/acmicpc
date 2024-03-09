#2nd_array + max value

#arr = [[0 for col in range(9)] for row in range(9)]

arr = [list(map(int, input().split())) for _ in range(9)]

max = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] >= max:
            max = arr[i][j]
            loc_y = i
            loc_x = j

print(max)
print(loc_y+1,loc_x+1)