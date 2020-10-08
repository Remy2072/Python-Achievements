import time
import os

factory = ["iphone"]
distribution = []
shop = []

def factory_to_distribution():
    distribution.extend(factory)
    factory.pop(0)


def distribution_to_shop():
    shop.extend(distribution)
    distribution.pop(0)

def printlist():
        print("factory = " + str(factory))
        print("distribution = "+ str(distribution))
        print("shop = "+ str(shop))
    
def nextprint():
    time.sleep(2)
    os.system('clear')

printlist()
factory_to_distribution()
nextprint()
printlist()
distribution_to_shop()
nextprint()
printlist()





