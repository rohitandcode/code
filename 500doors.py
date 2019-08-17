#500 doors and 500 people are present
#They are closed initially
#Each person goes through the doors and flips each door.
#1st person -> opens all doors
#2nd person -> goes to doors that are multiples of 2 -> 2,4,6,8, and flips them
#3rd person -> goes to doors that are multiples of 4 -> 4,8,12,16 and flips them

doors = [False] * 500
  
for i in range(500):
   for j in range(i, 500, i+1):
       doors[j] = not doors[j]
   if doors[i]:
       print ("Door %d:" % (i+1), 'open')
       
       
#Another way of doing this:
#Check for perfect squares, only perfect square will be open

for i in range(1,500):
    root = i**0.5
    if root == int(root):
        print ("Door %d:" % (i), 'open')
