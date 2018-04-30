# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:01:41 2018

@author: HXT
"""
""" 
For this challenge, create a bank account class that has two attributes:
    owner
    balance
  and two methods:
    deposit
    withdraw
As an added requirement, withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""

class Account:
    
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return (f"Account owner: {self.owner}\nAccount balance: ${self.balance}")
    
    def deposit(self, money):
        self.balance += money
        print("Deposit Accepted")
    
    def withdraw(self, money):
        if (money <= self.balance):
            self.balance -= money
            print("Withdraw Accepted")
        else:
            print("Funds Unavailable")


            