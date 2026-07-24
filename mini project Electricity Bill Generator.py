consumer_name = input("Enter Consumer Name: ")
units = int(input("Enter Units Consumed: "))

if units <= 100:
    bill = units * 5
else:
    bill = (100 * 5) + ((units - 100) * 10)

if units <= 100:
    subsidy = units * 5
else:
    subsidy = 100 * 5

bill_after_subsidy = bill - subsidy

gst = bill_after_subsidy * 0.18

final_bill = bill_after_subsidy + gst

print("Consumer Name :", consumer_name)
print("Units Consumed:", units)
print("Original Bill : ₹", bill)
print("Subsidy       : ₹", subsidy)
print("Bill After Subsidy : ₹", bill_after_subsidy)
print("GST (18%)     : ₹", round(gst, 2))

print("Total Payable : ₹", round(final_bill, 2))