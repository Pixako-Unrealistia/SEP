import ZODB, ZODB.config

import persistent
from abc import ABC, abstractmethod
import BTrees._OOBTree
import transaction
import z_obj
import os


path = os.path.join(os.path.dirname(__file__), 'config.xml')

db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root()

if __name__ == "__main__":
	root.customers = BTrees._OOBTree.OOBTree()
	root.customers["Dave"] = z_obj.Customer("Dave")
	d = root.customers["Dave"]
	root.customers["Jone"] = z_obj.Customer("Jone")
	j = root.customers["Jone"]

	print("Create Account:")
	b1 = d.addAccount(z_obj.SavingAccount(400, d))
	b2 = j.addAccount(z_obj.CurrentAccount(200, j))	
	d.printStatus()
	j.printStatus()

	print("\n Deposit 500 to account 2")
	b2.deposit(500)
	b2.printStatus()

	print("\n Withdraw 200 from account 1")
	b1.withdraw(200)
	b1.printStatus()

	print("\n Transfer 150 from account 2 to account 1")
	b2.transfer(150, b1)
	b1.printStatus()
	b2.printStatus()

	transaction.commit()