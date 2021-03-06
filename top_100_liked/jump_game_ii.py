class Solution:
    def jump(self, nums: List[int]) -> int:
        ### edge case
        if(len(nums) == 1):
            return 0
        count, cur = 0, 0
        while(cur != len(nums)-1):
            cur = self.jump_far(nums, cur)
            count += 1
        return count

    def jump_far(self, nums, cur):
        if(cur + nums[cur] >= len(nums)-1):
            return len(nums) - 1

        maxx, nxt = 0, 0
        for i in range(cur, cur+nums[cur]+1):
            if(nums[i] + i > maxx):
                maxx = nums[i] + i
                nxt = i
        return nxt
