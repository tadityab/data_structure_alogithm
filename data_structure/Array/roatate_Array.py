# Rotate Array
# Difficulty: MediumAccuracy: 37.06%Submissions: 436K+Points: 4
# Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.
#
# Note: Consider the array as circular.
#
# Examples :
#
# Input: arr[] = [1, 2, 3, 4, 5], d = 2
# Output: [3, 4, 5, 1, 2]
# Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.
# Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
# Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
# Explanation: when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.

#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, arr, d):
        #Your code here
        temp_arr = []
        for i in range(0,d):
            arr.append(arr[i])

        for i in range(d):
            arr.pop(0)


#{
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    # T = int(input())

    A = [i for i in "2 4 6 8 10 12 14 16 18 20".split(" ")]
    nd = [3]
    D = nd[0]
    ob = Solution()
    ob.rotateArr(A, D)

    for i in A:
        print(i, end=" ")

    print()

    # T -= 1

    print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
