nums = (1,4,9,16,25,36,49,64,81,100)

p = int(input("Enter the search element : "))
i=0
while i < len(nums):
    if(nums[i] == p):
        print("FOUND at index",i)
    i += 1 