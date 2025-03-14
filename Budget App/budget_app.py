class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount, 
            'description' : description
        })

        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({
            'amount': -1 * amount, 
            'description' : description
            })
            return True
        return False

    def get_balance(self):
        return sum([amount.get('amount') for amount in self.ledger])

    def transfer(self, amount, category):
        #withdraw amount
        #deposit new amount in category
        pass

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
    

def create_spend_chart(categories):
    pass


ledger = [
    {'amount': 20, 'description' : '1'},
    {'amount': 30, 'description' : '2'},
    ]

test = Category("Food")

test.deposit(30)

test.withdraw(40)


print(test.get_balance())
