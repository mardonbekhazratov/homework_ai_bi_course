def convert_cel_to_far(cel: float):
    return cel * 9 / 5 + 32

def convert_far_to_cel(far: float):
    return (far - 32) * 5 / 9


c = int(input("Enter a temperature in degrees F: "))
print(f"{c} degrees F = {convert_far_to_cel(c) : .2f} degrees C")

f = int(input("Enter a temperature in degrees C: "))
print(f"{f} degrees C = {convert_cel_to_far(f) : .2f} degrees F")
