import math
def hyp_calc(base:float, height:float) -> float:
    return(base**2 + height**2)**0.5

base = float(input("Base: "))
height = float(input("height: "))

print("Hypotenuse:", hyp_calc(base, height))