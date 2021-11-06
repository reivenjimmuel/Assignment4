def getUserInput():
    """ Function for money and cost input """
    money_ = float(input('Enter the amount of your money: '))
    cost_ = float(input('Enter the price of an apple: '))
    return money_, cost_
  
def amountAppleAndChange(money_, cost_):
    """ Function for computing the max number of apples
    and the total amount of change"""
    apple_ = int(money_/cost_)
    change_ = float(money_%cost_)
    return apple_, change_

def displayOutput(apples_, change_):
    print(f'You can buy {apples_} apples and your change is {change_:.2f} pesos.')

money, cost = getUserInput()
apple, change = amountAppleAndChange(money, cost)
displayOutput(apple, change)