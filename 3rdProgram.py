def getUserInput():

    """ Function for money and cost input and
     for computing the maximum amount of apples
     that you can buy and the amount of your change"""
     
    money_ = float(input('Enter the amount of your money: '))
    cost_ = float(input('Enter the price of an apple: '))
    apple_= int(money_/cost_)
    change_ = float(money_%cost_)
    return apple_, change_

def displayOutput(apples_, change_):
    print(f'You can buy {apples_} apples and your change is {change_:.2f} pesos.')

apples, change = getUserInput()
displayOutput(apples, change)