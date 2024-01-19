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

	b1 = d.addAccount(z_obj.SavingAccount(400, d))
	b2 = j.addAccount(z_obj.CurrentAccount(200, j))	

	b2.deposit(500)
	b1.withdraw(200)
	b2.transfer(150, b1)

	for customer in root.customers:
		obj = root.customers[customer]
		obj.printStatus()
		print()
		index = 0
		while obj.getAccount(index) != None:
			obj.getAccount(index).printTransaction()
			print("")
			index += 1

	transaction.commit()