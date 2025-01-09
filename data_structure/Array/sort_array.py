# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
#
# Note: The second largest element should not be equal to the largest element.
#
# Examples:
#
# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.
# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist.

# User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here

        arr.sort(reverse=True)
        for i in range(len(arr)-1):
            if arr[i] != arr[i+1]:
                return arr[i+1]

        return -1




# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    # t = int(input())
    # for _ in range(t):
    #     arr = list(map(int, input().split()))
    ob = Solution()
    arr = [12, 35, 1, 10, 34, 1]
    ans = ob.getSecondLargest(arr)
    print(ans)
    print("~")

    arr = [10, 5, 10]
    ans = ob.getSecondLargest(arr)
    print(ans)
    print("~")

    arr = [10, 10, 10]
    ans = ob.getSecondLargest(arr)
    print(ans)
    print("~")
# } Driver Code Ends