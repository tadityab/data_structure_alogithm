from array import array

if __name__ == '__main__':
    # Question 1: Create an array and traverse.
    arr1 = array('i',[1, 2, 3, 4, 5])
    for i in arr1:
        print(i)

    print("-"*50)
    # Question 2: Access individual elements through indexes.
    print(arr1[0])  # Output: 1
    print(arr1[2])  # Output: 3

    print("-"*50)
    # Question 3: Append any value to the array using append() method
    # array.append(): This method is used to add an element to the end of the array.
    # It takes a single argument, which is the value to be added.
    arr1.append(6)
    print(arr1)

    print("-"*50)

    # Question 4: Insert value in an array using insert() method
    # array.insert(): This method is used to insert an element at a specific position in the array.
    arr1.insert(3,7)
    print(arr1)

    print("-"*50)

    # Question 5: Extend python array using extend() method
    # array.extend(): This method is used to add multiple elements to the end of the array.
    arr1.extend([8, 9 , 10])
    print(arr1)

    print("-"*50)

    # Question 6: Add items from list into array using fromlist() method
    # array.fromlist(): This method is used to add items from a list to the end of the array.
    tempList = [20, 21, 22]
    arr1.fromlist(tempList)
    print(arr1)

    print("-"*50)

    # Question 7: Remove any array element using remove() method
    # array.remove(): This method is used to remove the first occurrence of a specified value from the array.
    arr1.remove(7)
    print(arr1)

    print("-"*50)

    # Question 8: Remove last array element using pop() method
    # array.pop(): This method is used to remove and return the last element from the array.
    arr1.pop()
    print(arr1)

    print("-"*50)

    # Question 9: Fetch any element through its index using index() method
    # array.index(): This method is used to find the index of the first occurrence of a specified value in the array.
    print(arr1.index(4))

    print("-"*50)

    # Question 10: Reverse a python array using reverse() method
    # array.reverse(): This method is used to reverse the order of the elements in the array.
    arr1.reverse()
    print(arr1)

    print("-"*50)

    # Question 11: Get array buffer information through buffer_info() method
    # array.buffer_info(): This method is used to get the memory address and the length of the array.
    print(arr1.buffer_info())

    # Question 12: Check for number of occurrences of an element using count() method
    # array.count(): This method is used to count the number of occurrences of a specified value in the array.
    arr1.fromlist(tempList)
    print(arr1)
    print(arr1.count(20))
    print(arr1.count(9))

    print("-"*50)

    # Question 13: Convert array to string using tostring() method
    # array.tostring(): This method is used to convert the array to a string representation.
    # arr1 = array('i',[1, 2, 3, 4, 5])
    # arr1_str = arr1.tostring()
    # print(arr1_str)
    #
    # print("-"*50)

    # Question 14: Convert array to a list using tolist() method
    # array.tolist(): This method is used to convert the array to a list.
    arr1_list = arr1.tolist()
    print(arr1_list)
    print(type(arr1_list))
    print("-"*50)

    # Question 15: Slice elements from an array
    # array slicing: This method is used to extract a portion of the array based on specified start and end indices.
    sliced_arr = arr1[2:5]
    print(sliced_arr)
    print(arr1[:])
    print("-"*50)
