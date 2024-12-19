def invest(amount, rate, years):
    for i in range(years):
        amount += amount * rate / 100
        print(f"Year {i+1}: ${amount : .2f}")

amount = int(input("Enter amount: "))
rate = int(input("Enter rate: "))
years = int(input("Enter years: "))

invest(amount,rate,years)