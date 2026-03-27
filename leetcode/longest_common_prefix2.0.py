class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for i in range(len(prefix)):
            for word in strs[1:]:
                if i >= len(word) or word[i] != prefix[i]:
                    return prefix[:i]
        return prefix

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["cat", "car", "candle"]))