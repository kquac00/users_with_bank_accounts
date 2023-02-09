class BankAccount:
    
    def __init__(self, int_rate= .1, balance = 100): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f"Insufficient funds: Charging a $5 fee{self.balance}")
            self.balance -= 5
        return self
    
        
    def display_account_info(self):
        print("Balance: ", self.balance)
        return self
        
    def yield_interest(self):
        
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
#***********************************************************************************


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = [BankAccount(int_rate=0.02, balance=100)]
        
    
    def add_account(self):
        #create an account
        new_account=BankAccount()
        #add new account to accounts attribute
        self.accounts.append(new_account)
        print(self.accounts)
        return self

    def make_deposit(self, amount, num=0):
        #select account from list
        selected_account = self.accounts[num]
        selected_account.deposit(amount)
        return self

    def make_withdrawal(self, amount, num=0):
        selected_account = self.accounts[num]
        selected_account.withdraw(amount)          
        return self
    
    def display_user_balance(self):
        print("Balance: ", self.accounts.display_account_info())
        return self

    # def transfer_balance(self, amount, num=0):
    #     selected_account = self.accounts[num]
    #     selected_account = self.accounts[num1]
    #     selected_account.transfer_balance()account[num1]
    #     print(f "{}")

user1 = User("Chris", "chrisa@yahoo.com")
# new account 1
user1.add_account()
# new account 2
user1.add_account()

user1.make_deposit(1000,0)
user1.make_deposit(2000,1)
user1.make_deposit(3000,2)
user1.accounts[0].display_account_info()
user1.accounts[1].display_account_info()
user1.accounts[2].display_account_info()
print("balance after withdrawal")
user1.make_withdrawal(200, 0)
user1.make_withdrawal(300, 1)
user1.make_withdrawal(400, 2)
user1.accounts[0].display_account_info()
user1.accounts[1].display_account_info()
user1.accounts[2].display_account_info()

#user1.transfer_balance(200, 0, 1)

