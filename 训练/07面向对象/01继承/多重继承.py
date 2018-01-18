# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:52:03 2018

@author: actionfocus
"""

#演示多重继承
#尽量不要在程序中启用多态继承，容易混淆类中的方法

import random

class Account(object):
    num_accounts = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1
    def __del__(self):
        Account.num_accounts -= 1
    def deposit(self, amt):
        self.balance = self.balance + amt
        print "from deposit(): " + str(self.balance)
    def withdraw(self, amt):
        self.balance = self.balance - amt
        print "from withdraw(): " + str(self.balance)
    def inquiry(self):
        return self.balance

class EvilAccount(Account):
    #重写了父类的inquiry方法
    def __init__(self, name, balance, evilfactor):
        super(EvilAccount,self).__init__(name, balance) #初始化Account
        self.evilfactor = evilfactor
        
    def inquiry(self):
        if random.randint(0,4) == 1:
            return self.balance * 1.1
        else:
            return self.balance

class DepositCharge(object):
    fee = 5.00
    def deposit_fee(self):
        print "This is from DepositCharge(): "+str(self.fee)

class WithdrawCharge(object):
    fee = 2.50
    def withdraw_fee(self):
        print "this is from  WithdrawCharge(): "+str(self.fee)
        
class MostEvilAccount(EvilAccount, DepositCharge, WithdrawCharge):
#    def __init__(self, name, balance, evilfactor):
#        super(MostEvilAccount,self).__init__(name, balance, evilfactor)
        
    def deposit(self, amt):
        self.deposit_fee()
        super(MostEvilAccount, self).deposit(amt)
    def withdraw(self, amt):
        self.withdraw_fee()
        super(MostEvilAccount, self).withdraw(amt)
        
if __name__ == '__main__':        
    d = MostEvilAccount("Dave", 500.00, 1.10)
    d.deposit_fee()
    d.withdraw_fee()
    d.deposit(400)
        
        