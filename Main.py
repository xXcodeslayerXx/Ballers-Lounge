def compoundinterest():
    age = int(input("when did you start investing? "))
    interest = float(input("What's the average annual interest return? "))
    amount = float(input("What's the amount you will invest every year? "))
    # finished all the inputs i need to complete this game/function
    add = (interest/100)  * (amount)
    total = (add) + (amount)
    # variables to calculate the first total
    print("age   amount   total")
    for counter in range (age, 61):
    # start of loop
        print(f'{counter}     {amount}    {round(total)}')
        add = (interest / 100) * (total)
        extra = (interest/100)  * (amount)
        total = (total) + (add) + (amount) + (extra)
        # end of the loop




def moneybuckets():
    income = float(input("What's your income? "))
    # only input needed to complete the game
    blow = float((income) * (60/100))
    daily = float((blow) * (60/100))
    splurge = float((blow) * (10/100))
    smile = float((blow) * (10/100))
    fire = float((blow) * (20/100))
    grow = float((income) * (20/100))
    mojo = float((income) * (20/100))
    # all the variables needed
    print(f"Blow = {blow} This should cover your daily expenses")
    print(f"Daily expense (60%) = {daily} ")
    print(f"Splurge (10%) = {splurge}")
    print(f"Smile (10%) = {smile}")
    print(f"Fire Extinguisher = {fire}")
    print(f"Grow (20% of Income) = {grow}")
    print(f"Mojo (20% of Income) = {mojo}")
    # end of money buckets



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
# added loop so there's a main menu and to give the user the option to either keep playing or to end game



