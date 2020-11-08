import values as v


def gettax(lst_bmgl):
    for i in v.steuersatz:
        if lst_bmgl <= i :
            tax = v.steuersatz[i]
            if lst_bmgl >= 83349.33:
                tax = 55

            return tax


def calctax(taxrate, lst_bmgl):
    totaltax = lst_bmgl * taxrate / 100
    return totaltax