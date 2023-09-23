time_float: float = float(input("Время до падения\n"))
where_hap_float: float = float(input("Какое ускорения свободного падения?(Зависит от спутника,планеты)\n"))

tall = (time_float**2) * where_hap_float/2

print(f'{time_float} секунд\n{where_hap_float} м/с**2')
print(tall)
