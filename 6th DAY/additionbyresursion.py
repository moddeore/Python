add = 0
def sum(n):
    if(n == 0):
        return 0
    add = n + sum(n-1)
    return add
p = int(input("Enter the number : "))
print(sum(p))