import ZODB, ZODB.config
import os
path = os.path.join(os.path.dirname(__file__), 'config.xml')

db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root()


import persistent
import pydantic
from abc import ABC, abstractmethod
import datetime
from enum import Enum

class Transaction_Type(Enum):
	DEPOSIT = "Deposit"
	WITHDRAW = "Withdraw"
	TRANSFER = "Transfer to"
	TRANSFER_IN = "Transfer from"
	def __str__(self):
		return self.value

class BankTransaction(persistent.Persistent):
	def __init__(self, amount = 0.0, old_balance = 0.0, new_balance = 0.0, timestamp = "", ttype = None, concerned_account = None):
		self.amount : float = amount 
		self.old_balance : float = old_balance
		self.new_balance : float = new_balance
		self.timestamp : str = timestamp
		self.ttype : Transaction_Type = ttype
		self.concerned_account : Account = concerned_account

	def printDetail(self):
		if (self.ttype == Transaction_Type.TRANSFER or self.ttype == Transaction_Type.TRANSFER_IN):
			print(f"{self.ttype} {self.concerned_account}:\nAmount : {self.amount}\nOld Balance : {self.old_balance}\nNew Balance : {self.new_balance}\nTime : {self.timestamp}")
		else:
			print(f"{self.ttype}:\nAmount : {self.amount}\nOld Balance : {self.old_balance}\nNew Balance : {self.new_balance}\nTime : {self.timestamp}")
		print()

class Customer(persistent.Persistent):
	def __init__(self, name = ""):
		self.name = name
		self.accounts = persistent.list.PersistentList()

	def __str__(self):
		return "Customer Name: " + self.name
	
	def addAccount(self, a):
		self.accounts.append(a)
		return (a)
	
	def getAccount(self, n):
		if 0 <= n < len(self.accounts):
			return (self.accounts[n])
		return None
	
	def printStatus(self):
		print(self.__str__())
		for a in self.accounts:
			print("", end="    ")
			a.printStatus()

class Account(ABC):
	def __init__(self, balance = 0.0, owner=None):
		self.balance = balance
		self.owner = owner
		self.BankTransaction : list = []

	@abstractmethod
	def __str__(self):
		pass

	def deposit(self, amount):
		self.BankTransaction.append(BankTransaction(amount, self.balance, self.balance + amount, datetime.datetime.now(), Transaction_Type.DEPOSIT))
		self.balance += amount
		return self.balance
	
	def withdraw(self, amount):
		self.balance -= amount
		return self.balance
	
	def transfer(self, amount, account):
		self.withdraw(amount)
		account.transferIn(amount)
		return self.balance
	
	def transferIn(self, amount, account):
		self.BankTransaction.append(BankTransaction(amount, self.balance, self.balance + amount, datetime.datetime.now(), Transaction_Type.TRANSFER_IN, account))
		self.balance += amount
	
	def accountDetail(self):
		return self.__str__() + " " + str(self.balance)
	
	def getBalance(self):
		return self.balance
	
	def printStatus(self):
		print("Account: " + self.__str__() + " " + str(self.balance))

	def printTransaction(self):
		for t in self.BankTransaction:
			t.printDetail()

class SavingAccount(Account, persistent.Persistent):
	def __init__(self, balance = 0.0, owner=None):
		Account.__init__(self, balance, owner)
		self.interest = 1.00

	def __str__(self):
		return self.owner.name
	
	def deposit(self, amount):
		self.BankTransaction.append(BankTransaction(amount, self.balance, self.balance + amount, datetime.datetime.now(), Transaction_Type.DEPOSIT))
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		if self.balance - amount >= 0:
			self.BankTransaction.append(BankTransaction(amount, self.balance, self.balance - amount, datetime.datetime.now(), Transaction_Type.WITHDRAW))
			self.balance -= amount
			return self.balance
		return None
	
	def transfer(self, amount, account):
		if self.balance - amount >= 0:
			self.BankTransaction.append(BankTransaction(amount, self.balance, self.balance - amount, datetime.datetime.now(), Transaction_Type.TRANSFER, account))
			self.balance -= amount
			account.transferIn(amount, self)
			return self.balance
		return None
	
	def printStatus(self):
		print( f"Saving Account of Customer : {self.owner.name} Balance {self.balance} Interest : {self.interest}")
	

class CurrentAccount(Account, persistent.Persistent):
	def __init__(self, balance = 0.0, owner=None):
		Account.__init__(self, balance, owner)
		self.limit = -5000.00

	def __str__(self):
		return self.owner.name
	

	def withdraw(self, amount):
		if self.balance - amount >= self.limit:
			self.BankTransaction.append(BankTransaction(amount, self.balance, self.balance - amount, datetime.datetime.now(), Transaction_Type.WITHDRAW))
			self.balance -= amount
			return self.balance
		return None
	
	def transfer(self, amount, account):
		if self.balance - amount >= self.limit:
			self.BankTransaction.append(BankTransaction(amount, self.balance, self.balance - amount, datetime.datetime.now(), Transaction_Type.TRANSFER, account))
			self.balance -= amount
			account.transferIn(amount, self)
			return self.balance
		return None
	
	def printStatus(self):
		print( f"Current Account of Customer : {self.owner.name} Balance {self.balance} Limit : {self.limit}")

		
		