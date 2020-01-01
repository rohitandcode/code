# "Alice likes Bob" transforms "Bob likes Alice"
  
# maybe seperate words by splitting with space

def rev(s):
    lis = s.split(" ")
    i = 0
    j = len(lis)-1
    while i < j:
        lis[i], lis[j] = lis[j], lis[i]
        i+=1
        j-=1
    return lis




s="Alice likes Bob"
print rev(s)

r = "zero one two three"
print rev(r)
