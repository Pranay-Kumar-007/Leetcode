class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                ans = nums[i] + nums[left] + nums[right]
                if ans==0:
                    out.append([nums[left],nums[i],nums[right]])
                    right-=1
                    left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                elif ans>0:
                    right-=1
                else:
                    left+=1
        return out
