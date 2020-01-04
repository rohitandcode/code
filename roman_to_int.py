class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicto = {'I':1,
             'V':5,
             'X':10,
             'L':50,
             'C':100,
             'D':500,
             'M':1000}
        lis = list(s)
        sums = 0
        for i in range(len(lis)):
            if lis[i] in dicto:
                if i > 0:
                    if dicto[lis[i-1]] < dicto[lis[i]]:
                        sums = sums + dicto[lis[i]] - 2*dicto[lis[i-1]]
                    else:
                        sums += dicto[lis[i]]
                else:
                    sums += dicto[lis[i]]
        return sums
        

"""
roman_to_int('III')
roman_to_int('VIII')
roman_to_int('IV')
roman_to_int('IX')
roman_to_int('XLIX')
"""
