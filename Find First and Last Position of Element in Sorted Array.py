class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos=[]
        for i in range(len(nums)):
            if nums[i]==target:
                pos.append(i)
        if len(pos)==0:
            pos.append(-1)
            pos.append(-1)
        else:
            pos=[min(pos),max(pos)]
        return pos
