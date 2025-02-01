nums = (1,4,9,16,25,36,49,64,81,100)
p = int(input("Enter the search element : "))
idx = 0
for el in nums:
    if(el == p):
        print("FOUND at index ",idx)
        break
    idx += 1
else:
        print("END") 