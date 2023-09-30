class Solution(object):
    def romanToInt(self,s):
        price={
                    "I":1,
                    "V":5,
                    "X":10,
                    "L":50,
                    "C":100,
                    "D":500,
                    "M":1000
                }
                
        total = 0
        i = 0

        while i < len(s):
                if i + 1 < len(s) and price[s[i]] < price[s[i + 1]]:
                    total += price[s[i + 1]] - price[s[i]]
                    i += 2  
                else:
                    total += price[s[i]]
                    i += 1

        return total

        result = romanToInt("MCMXCIV")
        print(result)
        