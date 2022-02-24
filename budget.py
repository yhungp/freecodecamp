from math import ceil

class Category(object):

    def __init__(self, category):
        self.category = category
        
        self.categories = {
            "food": 0, 
            "clothing": 0, 
            "entertainment": 0
        }
        
        self.all_deposits = 0
        self.get_balance = 0
        self.ledger = []

    def __repr__(self):
        char_before = (30 - len(self.category)) // 2
        top = "*" * char_before + self.category.capitalize() + "*" * (30 - char_before - len(self.category)) + "\n"
        
        
        description = lambda x : x + " " * (23 - len(x)) if len(x) < 23 else (str(x[:23]))
        amount = lambda x : " " * (7 - len("{x:.2f}".format(x=x))) + "{x:.2f}".format(x=x) if len("{x:.2f}".format(x=x)) < 7 else ("{x:.2f}".format(x=x))

        transactions = [ description(x['description']) + str(amount(x['amount'])) for x in self.ledger ]

        return "\n" + top + "\n".join(transactions) + "\nTotal: " + str(self.get_balance) + "\n"

    def deposit(self, amount, description=""):
        self.all_deposits += amount
        if len(self.ledger) == 0:
            description = "initial deposit" + " " * (30 - len("initial deposit") - len(str(self.all_deposits)))

        self.ledger.append({"amount": amount, "description": description})
        self.get_balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.get_balance -= amount
            return True

        else: return False

    def get_balance(self):
        return self.get_balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": "Transfer to " + str(category).capitalize()})
            self.get_balance -= amount
            category.deposit(amount, "Transfer from " + str(self.category).capitalize())
            return True

        else: return False

    def check_funds(self, amount):
        if amount < self.get_balance: return True
        else: return False



def create_spend_chart(categories: [Category]):
    spent = {}

    for cat in categories:
        spent[cat.category] = (abs(sum([x['amount'] for x in cat.ledger if x['amount'] < 0])), cat.all_deposits)

    for key in spent:
        a = spent[key]
        spent[key] = ceil(spent[key][0] / spent[key][1] * 100) // 10 * 10

    out = "Percentage spent by category\n"

    for i in range(10, -1, -1):
        circles = " "
        for key in spent:
            if spent[key] >= i * 10: 
                circles += "o  "
            else: 
                circles += "   "

        out += " " * (3 - len(str(i * 10))) + str(i * 10) + "|" + circles + " \n"
    
    out += " " * 4 + "-" * (1 + len(spent) * 3) + "\n"

    max_len = max([len(key) for key in spent])
    spent = [ (key + " " * (max_len - len(key))).capitalize() for key in spent ]

    out += "\n".join( [ " " * 5 + "".join([x[i]+ "  " for x in spent])  for i in range(max_len) ]) + "\n"

    return out
