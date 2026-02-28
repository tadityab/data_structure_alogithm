from array import array

if __name__ == '__main__':
    # Here
    # Time complexity : O(N)
    # Space complexity: O(1)
    # Point to remember
    # range and len function is having time complexity as O(1)

    arr1 = array('i', [1, 2, 3, 4, 5, 6])

    def linear_search(array, target):
        for i in range(len(array)):
            if array[i] == target:
                return i
        return -1


    print(linear_search(arr1, 5))
    print(linear_search(arr1, 8))
