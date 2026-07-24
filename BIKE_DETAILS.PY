
def bike_details(name, mf, price=50000):
    print("Bike Name       :", name)
    print("Manufacture Year:", mf)
    print("Selling Price   : ₹", price)
    print("-" * 30)

bike_details("Royal Enfield Classic 350", 2023, 210000)
bike_details("Yamaha R15 V4", 2024, 185000)
bike_details("KTM Duke 200", 2023, 200000)
bike_details("Bajaj Pulsar NS200", 2022, 160000)
bike_details("TVS Apache RTR 160", 2023, 145000)
bike_details("Hero Splendor Plus", 2024, 85000)
bike_details("Honda Shine", 2023, 90000)
bike_details("Suzuki Gixxer", 2022, 140000)
bike_details("Jawa 42", 2023, 195000)

bike_details("Old Bike", 2018)