'''
Temperature conversion program
'''

def celsiusToFarenheit():
    print(f"{'celsius':>10} {'farenheit':>10}")
    print(f"{'=======':>10} {'=========':>10}")

    for celsius in range(0, 101, 5):
        farenheit = celsius * 1.8 + 32
        print(f"{celsius:10} {farenheit:10.0f}")

def farenheitToCelsius():
    print(f"{'farenheit':>10} {'celsius':>10} ")
    print(f"{'=========':>10} {'=======':>10}")

    for farenheit in range(32, 222, 10):
        celsius = (farenheit - 32) / 1.8
        print(f"{farenheit:10} {celsius:10.1f} ")

celsiusToFarenheit()
print()
farenheitToCelsius()

