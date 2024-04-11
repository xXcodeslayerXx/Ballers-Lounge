def compoundinterest():
    age = int(input("when did you start investing ? "))
    interest = int(input("What's the average annual interest return ? "))
    amount = int(input("What's the amount you will invest every year ? "))
    add = (interest/100)  * (amount)
    total = (add) + (amount)
    for counter in range (age, 61):
        total = (total) + (amount)
        add = (interest) * (total)
        total = (total) + (interest)
        print (counter, amount, total)


compoundinterest()


