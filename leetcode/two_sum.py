def twoSum(self, nums, target):
        seen = {}
        for i,x in enumerate(nums):
            y = target - x
            if y in seen:
                return [seen[y], i]
            seen[x] = i

        return none