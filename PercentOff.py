price = float(input("How much is the original price? "))

percentOff = float(input("What percent off is it? ")) / 100

amountOff = price * percentOff

finalPrice = price - amountOff

finalPriceTax = finalPrice * 1.0625

print(f"${finalPriceTax} is the final price! (Including tax!)")

print("Thank you for using Percent-Off!")
