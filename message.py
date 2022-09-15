class Person:
    def __init__(self) -> None:
        self.first_name: str = ''
        self.last_name: str = ''
        self.age : int = 0
        self.country: str =''
        self.database: list = []

    def set_details(self):
        print('Please Enter your First_Name')
        first_name = str(input())
        if len(first_name) > 10 :
            print('please your name is too Long')
        else:
            self.first_name = first_name
            self.database.append(self.first_name)
        print('please Enter your Last_Name')
        last_name = str(input())
        if len(last_name) > 10 :
            print('Last_Name is too long')
        else:
            self.last_name = last_name
            self.database.append(self.last_nme)
        print('please Enter your age')
        age = int(input())
        if age < 18 : 
            print(f'you are not eligible for this offer {self.first_name} {self.last_name}')
        else:
            self.age = age
            self.database.append(age)
        print('please Enter your country of residence')
        country = str(input())
        self.country = country
        self.database.append(self.country)
    
obj = Person()

    