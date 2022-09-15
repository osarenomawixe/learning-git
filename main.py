class Banking:

    BANNED_COUNTRY = 'Nigeria'

    def __init__(self):
        self.first_name: str = ''
        self.last_name: str =''
        self.age: int = 0
        self.country: str = ''
        self.city: str = ''
        self.zip: str = ''
        self.Account_balance: int = 0.0
    
    def create_account(self):
        print('Enter your first Name')
        self.set_name = input()
        self.first_name = self.set_name

        print('Enter Last Namr ')
        self.set_last_name = input()
        self.last_name = self.set_last_name 

        print('Enter  Age')
        self.set_age = int(input())
        if self.set_age < 18 :
            print(f'hello {self.last_name} {self.first_name} you are too young to open an Account with us.')
            print('Thanks for comming')
        
        self.age = self.set_age

        print('Enter country')
        self.set_country = input()
        if self.set_country == Banking.BANNED_COUNTRY:
            print('You are not Eligible')
        self.country = self.set_country

        print('Enter Zip')
        self.set_zip =  input()
        self.zip = self.set_zip

        print('Enter City')
        self.set_city = input()
        self.city = self.set_city

    def deposit(self,Amount_to_deposit = None):
        print('type the amount you want to deposit')
        self.Amount_to_deposit = float(input)
        if self.Amount_to_deposit < 1000:
            print('The amount is Too small ')
        else:
            self.Account_balance += Amount_to_deposit
            print(f'you current balance is {self.Account_balance}')
    
    def withdraw(self):
        print('type the amount you want to withdraw')
        self.Amount_to_withdraw = float(input())
        self.Account_balance -= self.Amount_to_withdraw
        print(self.Account_balance)

obj = Banking()
obj.create_account()