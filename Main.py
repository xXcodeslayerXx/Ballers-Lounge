def compoundinterest():
    #
    age = int(input("when did you start investing? "))
    interest = int(input("What's the average annual interest return? "))
    amount = int(input("What's the amount you will invest every year? "))
    add = (interest/100)  * (amount)
    total = (add) + (amount)
    print("age   amount   total")
    for counter in range (age, 61):
        print(f'{counter}     {amount}    {round(total)}')
        add = (interest / 100) * (total)
        extra = (interest/100)  * (amount)
        total = (total) + (add) + (amount) + (extra)




def moneybuckets():
    income = int(input("What's your income? "))
    blow = (income) * (60/100)
    daily = (blow) * (60/100)
    splurge = (blow) * (10/100)
    smile = (blow) * (10/100)
    fire = (blow) * (20/100)
    grow = (income) * (20/100)
    mojo = (income) * (20/100)
    print(f"Blow = {blow} This should cover your daily expenses")
    print(f"Daily expense (60%) = {daily} ")
    print(f"Splurge (10%) = {splurge}")
    print(f"Smile (10%) = {smile}")
    print(f"Fire Extinguisher = {fire}")

    print(f"Grow (20% of Income) = {grow}")
    print(f"Mojo (20% of Income) = {mojo}")




print ('welcome to ballers lounge')
x = int(input ('select 1 for money buckets, 2 for compound interest, or 3 to end game: '))
while x != '':
    if x == 1:
        moneybuckets()
    if x == 2:
        compoundinterest()
    if x == 3:
        x = ''
    else:
        print ('Not valid selection')
        x = int(input('select 1 2 3'))



