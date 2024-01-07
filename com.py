code = """
length = int ( input ( ) )
width = int ( input ( ) )

area = length * width

print ( 3area )

"""


code_split = code.split()

key_words = [ 'int', 'input', 'print' ]

operators = [ '=', '*' ]

special_charecter = ['(', ')']

identifier = [ 'length', 'width', 'area' ]

for word in code_split :
    if word in key_words :
        print(f'{word} is a keyword\n')

    elif word in operators :
        print(f'{word} is a operator\n')

    elif word in special_charecter:
        print(f'{word} is a special charecter \n')

    elif word in identifier:
        print(f'{word} is a identifier \n')

    else :
        print(f'{word} is invalid !!! \n')
