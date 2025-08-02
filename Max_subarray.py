class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        current_arr = arr[0]
        max_arr = arr[0]
        for i in range(1,len(arr)):
            current_arr = max(arr[i],current_arr+arr[i])
            max_arr = max(current_arr,max_arr)
        return max_arr