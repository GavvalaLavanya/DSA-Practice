class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        k = 0
        for i in range(1,len(arr)):
            if arr[k] != arr[i]:
                k += 1
                arr[k] = arr [i]
        return k+1