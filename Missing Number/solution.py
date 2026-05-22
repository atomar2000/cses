import sys
input = sys.stdin.readline

inp = (int)(input())
list_inp = []

x = input()
list_inp = list(map(int, x.split()))

expected_sum = (int)((inp * (inp+1))/2)

actual_sum = 0

for item in list_inp:
    actual_sum = actual_sum + (int)(item)


print((int)(expected_sum-actual_sum))