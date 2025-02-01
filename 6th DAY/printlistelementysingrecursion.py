list = [1,2,3,4,5,6,7,8,9,10]
def show(list,idx=0):
    if(idx == len(list)):
        return
    print(list[0])
    show(list,idx+1)
print(list)