class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def no_pos_and_between_neg_is_zero(nums):
            for i in range(0, len(nums)):
                if nums[i] > 0:
                    return False
                elif nums[i] < 0:
                    if i != 0 and i != len(nums)-1 and (nums[i-1] != 0 or nums[i+1] != 0):
                        return False
                    elif i == 0 and nums[i+1] != 0:
                        return False
                    elif i == len(nums)-1 and nums[i-1] != 0:
                        return False
            return True
        if len(nums) == 1:
            return nums[0]
        if all(n == 0 for n in nums):
            return 0
        elif no_pos_and_between_neg_is_zero(nums):
            return 0
        cur_max = 1
        max_num = 1
        min_num = 1
        for n in nums:
            if n == 0:
                max_num = 1
                min_num = 1
            elif n > 0:
                max_num *= n
                min_num = min(min_num*n, 1)
            else:
                tmp_max = max_num
                max_num = max(min_num*n, 1)
                min_num = tmp_max*n
            cur_max = max(cur_max, max_num)
        return cur_max
        """
        # version 2, I came up with this solution but looked messy
        def compute_product(sublist, num_minus):
            update_cur_product = lambda x, y: x * y if x != -float("inf") else y
            ret = -float("inf")
            cur_product = -float("inf")
            cnt_minus = 0
            for n in sublist:
                if n < 0:
                    cnt_minus += 1
                    if cnt_minus == num_minus:
                        ret = max(ret, cur_product)
                        cur_product = -float("inf") # reset
                    else:
                        cur_product = update_cur_product(cur_product, n)
                else:
                    cur_product = update_cur_product(cur_product, n)
            return max(ret, cur_product)

        def max_left_right_product(sublist, num_minus):
            max_left_product = compute_product(sublist, num_minus)
            max_right_product = compute_product(sublist[::-1], num_minus)
            return max(max_left_product, max_right_product)
        
        def process_sublist(ret, sublist, num_minus):
            if num_minus and num_minus % 2 == 0:
                sub_product = 1
                for n in sublist:
                    sub_product *= n
                ret = max(ret, sub_product)
            else:
                ret = max(ret, *sublist, max_left_right_product(sublist, num_minus))
            return ret

        # the code starts here
        ret = -float("inf")
        sublist = []
        num_minus = 0
        for i in nums:
            if i == 0:
                ret = max(ret, 0)
                if not sublist:
                    continue
                ret = process_sublist(ret, sublist, num_minus)
                # reset
                num_minus = 0
                sublist = []
            else:
                sublist.append(i)
                if i < 0:
                    num_minus += 1
        
        
        ret = process_sublist(ret, sublist, num_minus)
        
        return ret
        """
        """
        # version 1, this DP method will MLE
        n = len(nums)
        dp = [[1] * n for _ in range(n)]
        ret = max(nums)
        for i in range(n):
            dp[i][i] = nums[i]
        
        for l in range(2, n+1):
            for i in range(0, n-l+1):
                j = i+l-1
                dp[i][j] = nums[i]*dp[i+1][j-1]*nums[j]
                if dp[i][j] > ret:
                    ret = dp[i][j]
        return ret
        """