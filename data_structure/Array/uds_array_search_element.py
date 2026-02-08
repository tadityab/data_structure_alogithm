from array import array

if __name__ == '__main__':
    arr1 = array('i', [1, 2, 3, 4, 5, 6])

    def linear_search(array, target):
        for i in range(len(array)):
            if array[i] == target:
                return i
        return -1


    print(linear_search(arr1, 5))
