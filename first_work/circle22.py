rad_int:  int = int(input("Radius\n"))
per_float: float = float(input("П\n"))

lenght = 2*rad_int*per_float
square = per_float*rad_int**2

print(f"{lenght} длина\n{square} площадь")
