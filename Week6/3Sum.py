class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums)-1):
            low, high, sum = i+1, len(nums) - 1,  0 - nums[i]
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                while(low < high):
                    if nums[low] + nums[high] == sum:
                        res.append([nums[i], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1

                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < sum:
                        low += 1
                    else:
                        high -= 1
        return res


