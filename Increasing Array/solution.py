n = (int)(input())

numbers = list(map(int,(input().split())))

max_val_idx = []

curr_max = -1

for num in numbers:
    max_val_idx.append(curr_max)
    curr_max = max(curr_max, num)


ans = 0

for i in range(0, n):
    if numbers[i] < max_val_idx[i]:
        ans = ans + (max_val_idx[i]-numbers[i])

print(ans)