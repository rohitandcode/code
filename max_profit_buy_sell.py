# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxi(prices):
    lowest = float('inf')
    target = 0
    try = 0
    for p in prices:
        lowest = min(p, lowest)
        target = max(target, p-lowest)
    return target

"""
arr=[7,1,5,3,6,4]
#arr=[7,6,4,3,1]
print (maxi(arr))
"""
