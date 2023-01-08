# getter setter method

# class one:
#     def __init__(self):
#         self.__car_company_name = 'Tata'
#         self.__bike_company_name = 'Honda'
#         self.car = 'mine'
#     def getter(self):
#         print('The car company is : ' + self.__car_company_name)
#         print('The car company is : ' + self.__bike_company_name)

#     def setter(self,car_name,bike_name):
#         self.__bike_company_name = bike_name
#         self.__car_company_name = car_name
#         # print('The car company is : ' + self.__car_company_name)
#         # print('The car company is : ' + self.__bike_company_name)
        

# obj = one()
# print(obj.car)

# obj.getter()
# obj.setter('M.G','KTM')
# obj.getter()



# method overloading

# from multipledispatch import dispatch

# @dispatch(str,str)
# def one(a,b):
#     print('this is for two strings')

# @dispatch(int,int)
# def one(a,b):
#         print('this is for two Numbers')


# one('one','two')
# one(1,2)



# has a relation

# class A:
#     def __init__(self):
#         self.name = 'rohan'

#     def one(self):
#         print('first class function.')

# class B:
#     def __init__(self):
#         self.a = A()

#     def one(self):
#         print('secound class function.')
#         self.a.one()

# obj=B()
# print(obj.a.name)



# abstraction 

# from abc import ABC,abstractmethod

# class Bank:

#     @abstractmethod
#     def check_balance(self):
#         pass
    
#     @abstractmethod
#     def withdraw_balance(self):
#         pass

#     @abstractmethod
#     def add_balance(self):
#         pass

# class Gpay(Bank):
#     def __init__(self):
#         self.balance = 1000

#     def check_balance(self):
#         print('Balance is : ',self.balance)

#     def withdraw_balance (self,amount):
#         self.balance = self.balance - amount

#     def add_balance(self,amount):
#         self.balance = self.balance + amount

# obj=Gpay()
# obj.check_balance()
# obj.add_balance(500)
# obj.check_balance()
# obj.withdraw_balance(500)
# obj.check_balance()


ls=[3,4,5,6,7]

d = {1,2,3,4}
d.add(3)
print(d)