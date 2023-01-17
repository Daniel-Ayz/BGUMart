from persistence import *

import sys


def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            product = repo.products.find(id=splittedline[0])[0]
            if int(splittedline[1]) > 0 or (int(splittedline[1]) < 0 and product.quantity >= -int(splittedline[1])):
                repo.activities.insert(Activitie(*splittedline))
                repo.products.update({"quantity": str(product.quantity + int(splittedline[1]))}, {"id": str(splittedline[0])})


if __name__ == '__main__':
    main(sys.argv)