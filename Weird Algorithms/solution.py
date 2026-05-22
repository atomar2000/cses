inp = (int)(input())

def weird_algorithm(n):
    if n % 2 == 1:
        return (n * 3) + 1
    else: 
        return n/2
        
while(inp):
    new_val = (int)(weird_algorithm(inp))
    print(inp, end=" ")
    if inp == 1:
        break
    inp = new_val
    