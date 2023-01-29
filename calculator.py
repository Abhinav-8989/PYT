print("Welcome To Virtual Calculator")
def calculate():
    
    operation = input('''
Please Select:
+ for addition
- for subtraction
* for multiplication
/ for division
  First You Have To Enter The Operand:
''')
     #First Value
    n1 = int(input('Enter First Value: '))
    # Second Value
    n2 = int(input('Enter Second Value: '))
    # String Formatters With COnditional Statement
    if operation == '+':
        print('{} + {} = '.format(n1, n2))
        print(n1 + n2)

    elif operation == '-':
        print('{} - {} = '.format(n1, n2))
        print(n1 - n2)

    elif operation == '*':
        print('{} * {} = '.format(n1, n2))
        print(n1 * n2)

    elif operation == '/':
        print('{} / {} = '.format(n1, n2))
        print(n1 / n2)

    else:
        print('You have not typed a valid operator, please run the program again.')

  

calculate()