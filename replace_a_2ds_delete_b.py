# From EPI
# ex array = [a,c,d,b,b,c,a] results [d,d,c,d,c,d,d]
# ex array = [a,b,a,c,space] and size is 4 -> results [d,d,d,d,c]

def convert_arr(arr):
    lens = len(arr)
    for j in range(2):
        print "try {}".format(j)
        for i in range(lens):
            if arr[i] == 'a':
                arr.pop(i)
                arr.insert(i, 'd')
                arr.insert(i+1, 'd')
            elif arr[i] == 'b':
                arr.pop(i)
    return arr


arr = ['a','c','d','b','b','c','a']
print convert_arr(arr)

arr2 = ['a','b','a','c', ]
print convert_arr(arr2)

"""
try 0
try 1
['d', 'd', 'c', 'd', 'c', 'd', 'd']
try 0
try 1
['d', 'd', 'd', 'd', 'c']
"""
