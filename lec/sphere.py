PI = 3.14



def main():
    radius = float(input())
    
    if radius < 0:
        print("INVALID")
    else:
        print(f"VOLUME: {calc_volume(radius)} cubic units")
        print(f"SURFACE AREA: {calc_surface_area(radius)} square units")
        print(f"DIAMETER: {calc_diameter(radius)} units")
    
    

def calc_volume(radius):
    volume = (4/3) * (PI) * (pow(radius,3))
    return round(volume,2)


def calc_surface_area(radius):
    surface_area = (4) * (PI) * (pow(radius,2))
    return round(surface_area,2)


def calc_diameter(radius):
    diameter = (radius) * (2)
    return round(diameter,2)



main()
