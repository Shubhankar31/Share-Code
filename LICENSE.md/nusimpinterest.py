
print("please put the values in decimal.")



amount = float(input("Put Amount: "))
rate = float(input("Put Rate of interest without %: "))
time = float(input("Put Time in year(/s)): "))

print(amount, rate, time)
simple_interest = amount * rate * time / 100
print(type(simple_interest))
print("Your simple interest is", simple_interest)
print("Your total amount is", simple_interest + amount)
