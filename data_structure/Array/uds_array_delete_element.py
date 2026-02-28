from array import array

if __name__ == '__main__':
    # Here
    # Time complexity : Can very if we delete the last element then O(1) else O(N)
    # Space complexity: O(1)

    arr1 = array('i', [1, 2, 3, 4, 5, 6])

    arr1.remove(3)

    print(arr1)