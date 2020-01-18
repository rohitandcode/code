""" Given a list, with 3 conditions:
1. there will be one unique num and multiple pairs
2. positive nums
3. only one unique
Find the unique num and ints index"

l1 = [11,12,11,12,1,5,5]
  
l2 = list(l1) #making a copy of the list

print l2
d1 = {} #creating a dictionary to create the data of repeated and unique nums
for i in range(len(l1)-1):
    if l1[i] not in d1:
        d1[l1[i]] = 1
        index = i
    else:
        d1[l1[i]] += 1
    l2.remove(l1[i])
    if l1[i] not in l2 and d1[l1[i]] == 1:
        print "-->{},index:{}".format(l1[i],i)
