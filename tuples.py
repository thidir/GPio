
def partition(num1):
    if num1 % 2 ==0:
        return(num1,None)
    else:
        return(None,num1)


Finallist=[]
def partition_list(the_list):
    for i in the_list:
        Finallist.append(partition(i))
    return Finallist


the_list=[1,2,3,4,5,6,7,8,9,10]

b = partition_list(the_list)

for  item in b:
    print(item)
