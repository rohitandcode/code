def my4_remove_duplicates(lst):
    lst.sort()
    i = len(lst) - 1
    while i > 0:  
        if lst[i] == lst[i - 1]:
            lst.pop(i)
        i -= 1
    return lst
    
lst = [1,3,3,0,15,-1,0,1,1]
my4_remove_duplicates(lst)
