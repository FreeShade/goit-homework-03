base_rate = 40
price_per_km = 10
total_trip = 0


def trip_price(path):
    global total_trip
    total_trip += 1
    print(total_trip)
    sum = path * 10 + 40
    return sum
