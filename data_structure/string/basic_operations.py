if __name__ == '__main__':
    # creating a string
    s1 = 'GfG'
    print(s1)
    s1 = """I am Learning 
    Data structure - String"""
    print(s1)

    print("-----------------Access string")
    # Accessing characters in python
    s = 'Learning DataStructure'
    print(s[0]) # access zero index character i.e. first character

    print("-----------------Access using negative index")
    print(s[-2]) # access second last element from the string .

    print("-----------------Slicing string")
    s = "Learning Data Structure"
    print(s[:2]) # Retrieve the characters from 0 to 1.

    print(s[1:4]) # Retrieve characters from 1 to 3

    print(s[3:]) # retrieve character from 3 to end

    print(s[::-1]) # reverse the string

    print("-----------------Deletion string")
    s = "GfG"
    del s
    # print(s)

    print("-----------------Update string")
    # make first letter to upper case.
    s = "hello DS"
    print("H" + s[1:])

    # replace DS with Data Structure
    s1 = s.replace("DS","Data Structure")
    print(s1)

