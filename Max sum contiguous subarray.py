Find the contiguous subarray within an array, A of length N which has the largest sum.

Input Format:

The first and the only argument contains an integer array, A.
Output Format:

Return an integer representing the maximum possible sum of the contiguous subarray.

===============================================================================================================================
class Solution:
    # @param A : tuple of integers
    # @return an integer

    def maxSubArray(self, a):
        mx = a[0]
        curr_max = a[0]

        for i in range(1, len(a)):
            curr_max = max(a[i], curr_max + a[i])
            mx = max(mx, curr_max)

        return mx
