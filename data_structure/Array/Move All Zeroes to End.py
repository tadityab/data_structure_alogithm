# You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.
#
# Examples:
#
# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.
# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]
# Explanation: No change in array as there are no 0s.
# Input: arr[] = [0, 0]
# Output: [0, 0]
# Explanation: No change in array as there are all 0s.
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 105

#User function Template for python3

class Solution:
    def pushZerosToEnd(self,arr):
        temp_arr = [0] * len(arr)
        cnt = 0
        for i in range(len(temp_arr)):
            if arr[i] != 0:
                temp_arr[cnt] = arr[i]
                cnt += 1
        return temp_arr


if __name__ == '__main__':
    # tc = int(input())
    # while tc > 0:
    #     arr = list(map(int, input().strip().split()))
    arr = [3,5 ,0 ,0 ,4]
    ob = Solution()
    result = ob.pushZerosToEnd(arr)
    for x in arr:
        print(x, end=" ")
    print(result)

# } Driver Code Ends

# result = [x for x in my_list if x != 0] + [0] * my_list.count(0)