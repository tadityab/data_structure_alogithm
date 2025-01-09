
if __name__ == '__main__':

    # 1. Array Traversal
    print("------------------------Array Traversal")
    lst = [1,2,3,4,5]

    for i in lst:
        print(i)

    for i in range(len(lst)):
        print(lst[i])

    print("------------------------Insertion in Array")
    lst = [1,2,3,4,5]

    # This will append are at the end of the list.
    lst.append(4)
    print(lst)

    # Insert element at specific location
    lst.insert(1, 5) # insert 5 at index 1
    print(lst)

    print("------------------------Deletion in Array")
    lst = [1,2,3,4,5,6,7]

    # Remove the first occurrence of a specific value.
    lst.remove(2) # Removes the fist occurence of 2
    print(lst)

    lst = [1, 2, 3, 4, 5, 6, 7]
    # Remove and returns an element at a specific index (or the last element by default)
    removed_element = lst.pop(2)
    print(f"Removed element : {removed_element}")
    print(lst)
    lst = [1, 2, 3, 4, 5, 6, 7]
    del lst[2] # remove second index element
    print(lst)

    print("------------------------Searching element")
    lst = [1, 2, 3, 4, 5, 6, 7]
    for i in lst:
        if i == 2:
            print(f"value is present: {i}")

    for i in range(len(lst)):
        if lst[i] == 2:
            print(f"value {lst[i]} is present at index : {i}")

    for i, value in enumerate(lst):
        if value == 2:
            print(f"value {value} is present at index : {i}")