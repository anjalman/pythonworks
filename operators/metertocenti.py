def meter_to_centimeters(meter):

    centimeters = meter * 100

    return centimeters

meter=float(input("enter the deistance in meter:"))

centimeter = meter_to_centimeters(meter)

print(f"{meter} is equal to {centimeter} centimeter")



