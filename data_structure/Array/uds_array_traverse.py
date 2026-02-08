from array import array

if __name__ == '__main__':

    # Traverse Array: Means visiting each element in an array
    # Time complexity:  o(n)
    # Space complexity: o(1)
    arr1 = array('i',[1,2,3,4,5,6])

    def traverseArray(array):
        for i in array:       # O(n)             O(n) + O(1) = O(n)
            print(i)          # O(1)

    traverseArray(arr1)