
def getUserInput():
    """ Function for name, age, and address in input"""
    name_ = input('Enter your Full Name: ')
    age_ = int(input('Enter your Age: '))
    address_ = input('Enter yout Address: ')
    return name_, age_, address_

def displayOutput(name_, age_, address_):
    print(f'Hi, my name is {name_}. I am {age_} years old and I live in {address_}.')

# Steps:
# Ask for name, age and address
name, age, address = getUserInput()
# Display name, age, and address
displayOutput(name, age, address)