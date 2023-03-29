radius = float(input())
 
    
if radius < 0:
    print("INVALID")
else:
    PI = 3.14


    volume = (4/3) * (PI) * (pow(radius,3))
    volume = round(volume,2)

    surface_area = (4) * (PI) * (pow(radius,2))
    surface_area = round(surface_area,2)

    diameter = (radius) * (2)
    diameter = round(diameter,2)


    print(f"VOLUME: {volume} cubic units")
    print(f"SURFACE AREA: {surface_area} square units")
    print(f"DIAMETER: {diameter} units")
