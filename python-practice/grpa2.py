# Input values
a = 6
price1, discount1 = 50, 4
price2, discount2 = 60, 8

# Solutions
output1 = a >= 5

output2 = a % 5 == 0

output3 = a % 2 == 1 and a < 10

output4 = a % 2 == 1 and a > -10 and a < 10

output5 = len(str(abs(a))) % 2 == 0 and len(str(abs(a))) <= 10

is_offer1_cheaper = price1 * (1 - discount1/100) < price2 * (1 - discount2/100)

# Print results
print("output1:", output1)
print("output2:", output2)
print("output3:", output3)
print("output4:", output4)
print("output5:", output5)
print("is_offer1_cheaper:", is_offer1_cheaper)