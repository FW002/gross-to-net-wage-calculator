import numpy as np
import time
import values as v
from avab import gettax, calctax
import django.db
from overtime import calcovertime


def november():
    return True

def grossPP():
    return True

print(">Hallo, bitte beantworte folgende Fragen")
print(">Ist der Monat November? [y/n]: ")
userMonth = input(">")

nov = False
grPP = False

if userMonth == "y":
    nov = november()

print(">Dein Bruttogehalt: ")
brutto = input(">")
int(brutto)

print(">Anzahl der Kinder: ")
children = input(">")

print(">Pendlerkilometer: ")
pendlerkm = input(">")

print(">Große Pendlerpauschale? [y/n]: ")
gr = input(">")

if gr == "y":
    grPP = grossPP()

print(">Anzahl der Überstunden:")
overtime = input(">")
bruttoOvertimeSalary, taxfreeOvertime = calcovertime(overtime, brutto, divider=158)
print(bruttoOvertimeSalary)
print(taxfreeOvertime)
print("------")

#Höchstbetrag?-------------------------------------------------
if int(brutto) > v.GLOBAL_sv_hoechstbetrag:
    diff = v.GLOBAL_sv_hoechstbetrag - int(brutto)
    brutto = int(brutto) - diff

# Rechnung LST_BMGL-------------------------------------------------------
print("> Brutto:              ", int(brutto), "€")
sv = (int(brutto) * v.GLOBAL_sv) / 100
print("> SV:                  ", "-", sv, "€")
print("> Gewerkschaft:        ", "-",v.GLOBAL_gewerkschaft, "€")
print("> Freibetrag:          ", "-",v.GLOBAL_fb, "€")
lst_bmgl = int(brutto) - sv - v.GLOBAL_gewerkschaft - v.GLOBAL_fb

if nov == True:
    print("> E-Card:              ", "-",v.GLOBAL_ecard, "€")
    lst_bmgl = lst_bmgl - v.GLOBAL_ecard


print("------")

# LST_BMGL Ausgabe-------------------------------------
print(">LST_BMGL: ", round(lst_bmgl, 3), "€")

taxrate = gettax(lst_bmgl)
print("Lohnsteuersatz: ", taxrate, "%")

totaltax = calctax(taxrate, lst_bmgl)
print("Lohnsteuer:  ", round(totaltax,3), "€")

print("---------- NETTO -------------")

print("> Brutto:              ", int(brutto), "€")
print("> SV:                  ", "-", sv, "€")
print("> Gewerkschaft:        ", "-",v.GLOBAL_gewerkschaft, "€")
print("> Lohnsteuer:          ", "-",totaltax, "€")
netto = int(brutto) - sv - v.GLOBAL_gewerkschaft - totaltax

if nov == True:
    print("> E-Card:              ", "-",v.GLOBAL_ecard, "€")
    netto = netto - v.GLOBAL_ecard

print("Nettobetrag:     ", round(netto, 3), "€")

#print(v.smallPP[0])