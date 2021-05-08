spending = [140, 30, 999, 145, 538, 878, 901, 613, 471, 286, 147, 90]
income = [300, 40, 0, 4000, 8911, 73, 85, 0, 9000, 941, 658, 190]

coefficients = []
for i in range(12):
    try:
        coefficients.append(spending[i]/income[i])
    except ZeroDivisionError:
        continue
    finally:
        coefficients.append(0)
print(coefficients)
year_coefficient = sum(coefficients) / 12
print('Средний коэффициент распределения расходов за год: ', round(year_coefficient, 2))
