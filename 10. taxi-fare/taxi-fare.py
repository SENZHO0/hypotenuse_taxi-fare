import math
base = 4
plus = 0.25
def taxi_fare(distance:float) -> float:
    plus_2 = ((distance_km*1000)/140)*plus
    return(base + plus_2)

distance_km = float(input("Distance in KM: "))
print("Total: $", taxi_fare(distance_km))