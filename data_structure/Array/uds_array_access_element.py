from array import array

if __name__ == '__main__':
    # Access Array Element based on Index
    # Time Complexity    :  O(1)
    # Space Complexity   :  O(1)


    arr1 = array('i', [1, 2, 3, 4, 5, 6])
    print(len(arr1))


    def access_element(array, index):
        if index >= len(array):                                # O(1)    O(1) + O(1) + O(1) = O(1)
            print('Given Index is not present in the Array')   # O(1)
        else:
            print(array[index])                                # O(1)


    access_element(arr1, 4)

    access_element(arr1, 7)
