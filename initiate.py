from persistence import *

import sys
import os


def add_branche(splittedline: list[str]):
    repo.branches.insert(Branche(*splittedline))


def add_supplier(splittedline: list[str]):
    repo.suppliers.insert(Supplier(*splittedline))


def add_product(splittedline: list[str]):
    repo.products.insert(Product(*splittedline))


def add_employee(splittedline: list[str]):
    repo.employees.insert(Employee(*splittedline))


adders = {"B": add_branche,
          "S": add_supplier,
          "P": add_product,
          "E": add_employee}


def main(args: list[str]):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    # uncomment if needed
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline: list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])


if __name__ == '__main__':
    main(sys.argv)
