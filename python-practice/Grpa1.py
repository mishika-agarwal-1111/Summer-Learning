# Input values (change these to test different cases)
a = 5
b = 6
price, discount_percent = 80, 5.75
total_mins = 470

# Solutions
output1 = a + b
output2 = 2 * (a + b)
output3 = abs(a - b)
output4 = abs((a + b) - (a * b))

discounted_price = price * (1 - discount_percent / 100)
rounded_discounted_price = round(discounted_price)

hrs = total_mins // 60
mins = total_mins % 60

# Print to see results
print("output1:", output1)
print("output2:", output2)
print("output3:", output3)
print("output4:", output4)
print("discounted_price:", discounted_price)
print("rounded_discounted_price:", rounded_discounted_price)
print("hrs:", hrs)
print("mins:", mins)