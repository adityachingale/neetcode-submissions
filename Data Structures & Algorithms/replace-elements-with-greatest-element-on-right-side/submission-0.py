class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVal = -1
        n = len(arr) - 1
        for i in range(n, -1, -1):
            savedVal = arr[i]
            arr[i] = maxVal
            maxVal = max(maxVal, savedVal)
        return arr
