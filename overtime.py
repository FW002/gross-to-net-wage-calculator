import values

def calcovertime(overtimehours, brutto, divider):
    hourlySalary = int(brutto) / divider
    bruttoOvertimeSalary = float(overtimehours) * hourlySalary
    overtimeBonus = 50 * hourlySalary / 100
    if float(overtimehours) >= 10:
        taxFreeOvertime = 10
        taxedOvertime = float(overtimehours) - taxFreeOvertime

    taxFreeOvertimeSalary = overtimeBonus * 10 #Lohnsteuerfrei
    taxedOvertime = overtimeBonus

    bruttoOvertime = taxedOvertime + taxFreeOvertimeSalary
    return bruttoOvertime, taxFreeOvertimeSalary