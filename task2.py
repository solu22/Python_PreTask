''' Implement a Python function that returns the balance of a bank account as an integer, based on a list of transactions. 
The balance of the account is 0 at the beginning.

Format of the transactions list:

    transactions = [
        "W 200",
        "D 100
    ]
Where W = withdraw, and D = deposit. For example, for

    transactions = [
        "D 300",
        "D 300",
        "W 200",
        "D 100",
    ]
the balance of the bank account should be 500 '''

#function defination

def account_balance(transaction):
  # required variables initialization
    balance = 0

    # looping through transcation
    for element in transaction:
        
        # upadate balance with deposite
        if element.split()[0] == 'D':
            balance =  balance + int(element.split()[1])
        
         # upadate balance with withdraw
        if element.split()[0] == 'W':
            balance =  balance - int(element.split()[1])

    # current balance      
    return balance

if __name__ == '__main__':
    transaction = ["D 300", "D 300","W 800","D 100"]
    getBalance = account_balance(transaction)
    print('The current balance is: {}'.format(getBalance))