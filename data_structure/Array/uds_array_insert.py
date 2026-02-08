import array

if __name__ == '__main__':
    # inserting element at the starting of the array
    my_array = array.array('i',[1,2,3,4,5])
    print(my_array)

    #Inserting element at the starting position of the array,
    #In this case all the elements will be shifted to next position
    my_array.insert(0,6)
    print(my_array)

    #Inserting element at the middle position of the array,
    #still remaining element of the array will be shifted to the next position
    my_array.insert(3,6)
    print(my_array)

    #Inserting element of the end position, will not shift any elements
    #This will be faster as compare to above insert type
    my_array.insert(5,6)
    print(my_array)

    #Here at position instead of giving 6, we can give any value like 100 still element will be inserted at the end of the element
    my_array.insert(100,6)
    print(my_array)

    my_array.insert(90,7)
    print(my_array)