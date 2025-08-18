
def usd_to_sgd(usd, rate):
    return usd * rate

usd = float(input("Enter amount in usd:"))
rate = float(input("Enter USD to SGD rate:"))

sgd = usd_to_sgd(usd, rate)
print("Amount in SGD:", round(sgd, 2))