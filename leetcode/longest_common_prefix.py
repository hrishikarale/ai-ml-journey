class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for word in strs:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix

if __name__ == "__main__":
sol = Solution()
print(sol.longestCommonPrefix(["cat", "car", "candle"]))
