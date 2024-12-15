"""
Steps as per 'https://www.programiz.com/dsa/algorithm'
Step 1: Start
Step 2: Declare variables a,b and c.
Step 3: Read variables a,b and c.
Step 4: If a > b
           If a > c
              Display a is the largest number.
           Else
              Display c is the largest number.
        Else
           If b > c
              Display b is the largest number.
           Else
              Display c is the greatest number.
Step 5: Stop
"""

if __name__ == '__main__':
    # Initialize variable with the input value
    input1 = int(input("Provide first input number: "))
    input2 = int(input("Provide second input number: "))
    input3 = int(input("Provide third input number: "))

    # Main logic
    if input1 > input2:
        if input1 > input3:
            print(f"input1 {input1} is greater number.")
        else:
            input(f"input3 {input3} is greater number.")
    else:
        if input2 > input3:
            print(f"input2 {input2} is greater number.")
        else:
            print(f"input3 {input3} is greater number.")
