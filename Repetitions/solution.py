inp = input()
n = len(inp)

ans = 1
i = 0

while i < n-1:
    if inp[i] == inp[i+1]:
        curr_ans = 1
        j = i+1
        while j < n:
            if inp[j] == inp[i]:
                curr_ans = curr_ans + 1
            else:
                break
            j = j + 1
        i = j-1
        ans = max(ans, curr_ans)
    else:
        i = i + 1

print(ans)