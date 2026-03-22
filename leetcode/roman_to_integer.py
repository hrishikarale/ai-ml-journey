class Solution:
    def romanToInt(self,s):
        roman_values = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        total = 0
        i = 0
        while i < len(s):
            current_value = roman_values[s[i]]
            if i+1 < len(s) and current_value < roman_values[s[i+1]]:
                total += roman_values[s[i+1]] - current_value
                i += 2 
            else:
                total += current_value
                i += 1
        return total
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("DM"))
    print(sol.romanToInt("LVIII"))
    print(sol.romanToInt("MCMXCIV"))




