print("Welcome to the tip calculator")
print("What was the total bill? $")
bill = int(input())
print("What percentage tip would you like to give? 10, 12, or 15?")
percentage = int(input())
print("How many people will split the bill?")
num = int(input())

print("Each person should pay : ")
tip = bill * (percentage/100)
final_bill = bill + tip
perperson = final_bill / num

print(float(perperson))