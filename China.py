#Program: china.py
#Author: Mitchell Krystofiak
#Description: This program grabs data associated with the N economy
#             of China, including(not limited to):
              # -crops -yield(and all input variables)
              # -NUE -GDP -population -imports

#Last Edited: Monday, April 12, 2021

import scipy
import scipy.io
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

obj = scipy.io.loadmat("iFarmData(2015)_1_28_2019.mat")

china_i  = int(np.where(obj['FAOSTAT_CoName_FAO'] == "China")[0]) #39
numCrops = max(obj['FAOSTAT_CrName_FAO'].shape)
numCos = max(DATA['FAOSTAT_CoName_FAO'].shape)

yr = int(input("Enter the year you would like to receive data for: "))
while yr < 1961 or yr > 2015:
    if yr < 1961:
        print("Invalid year. Lowest year possible is 1961.")
        yr = int(input("Enter the year you would like to receive data for: "))
    elif yr > 2015:
        print("Invalid year. Highest year possile is 2015.")
        yr = int(input("Enter the year you would like to receive data for: "))

print()
print("Country: China")
print("Year   : ", yr)

_yr = int(np.where(obj['Yr'][0] == yr)[0])

chaRice_i = int(np.where(obj['FAOSTAT_CrName_FAO'] == "Rice; paddy")[0])
chaPeas_i = int(np.where(obj['FAOSTAT_CrName_FAO'] == "Peas; green")[0])
chaSuga_i = int(np.where(obj['FAOSTAT_CrName_FAO'] == "Sugar cane")[0])
chaMush_i = int(np.where(obj['FAOSTAT_CrName_FAO'] == "Mushrooms and truffles")[0])


chaRiceNYield = obj['Nyield_kgkm'][china_i][chaRice_i][_yr]
chaPeasNYield = obj['Nyield_kgkm'][china_i][chaPeas_i][_yr]
chaSugaNYield = obj['Nyield_kgkm'][china_i][chaSuga_i][_yr]
chaMushNYield = obj['Nyield_kgkm'][china_i][chaMush_i][_yr]

chaRiceNfer = obj['Nfer_kgkm'][china_i][chaRice_i][_yr]
chaPeasNfer = obj['Nfer_kgkm'][china_i][chaPeas_i][_yr]
chaSugaNfer = obj['Nfer_kgkm'][china_i][chaSuga_i][_yr]
chaMushNfer = obj['Nfer_kgkm'][china_i][chaMush_i][_yr]

chaRiceNman = obj['Nman_kgkm'][china_i][chaRice_i][_yr]
chaPeasNman = obj['Nman_kgkm'][china_i][chaPeas_i][_yr]
chaSugaNman = obj['Nman_kgkm'][china_i][chaSuga_i][_yr]
chaMushNman = obj['Nman_kgkm'][china_i][chaMush_i][_yr]

chaRiceNdep = obj['Ndep_kgkm'][china_i][chaRice_i][_yr]
chaPeasNdep = obj['Ndep_kgkm'][china_i][chaPeas_i][_yr]
chaSugaNdep = obj['Ndep_kgkm'][china_i][chaSuga_i][_yr]
chaMushNdep = obj['Ndep_kgkm'][china_i][chaMush_i][_yr]

chaRiceNUE = obj['NUE_3d'][china_i][chaRice_i][_yr]
chaPeasNUE = obj['NUE_3d'][china_i][chaPeas_i][_yr]
chaSugaNUE = obj['NUE_3d'][china_i][chaSuga_i][_yr]
chaMushNUE = obj['NUE_3d'][china_i][chaMush_i][_yr]

chaRiceNfer = obj['Nfer_kgkm'][china_i][chaRice_i][_yr]
chaPeasNfer = obj['Nfer_kgkm'][china_i][chaPeas_i][_yr]
chaSugaNfer = obj['Nfer_kgkm'][china_i][chaSuga_i][_yr]
chaMushNfer = obj['Nfer_kgkm'][china_i][chaMush_i][_yr]

chaRiceNexc = obj['Nexc_kgkm'][china_i][chaRice_i][_yr]
chaPeasNexc = obj['Nexc_kgkm'][china_i][chaPeas_i][_yr]
chaSugaNexc = obj['Nexc_kgkm'][china_i][chaSuga_i][_yr]
chaMushNexc = obj['Nexc_kgkm'][china_i][chaMush_i][_yr]

chaRiceY = obj['Yield_FAO'][china_i][chaRice_i][_yr]
chaPeasY = obj['Yield_FAO'][china_i][chaPeas_i][_yr]
chaSugaY = obj['Yield_FAO'][china_i][chaSuga_i][_yr]
chaMushY = obj['Yield_FAO'][china_i][chaMush_i][_yr]

chaRiceA = obj['AreaH_FAO'][china_i][chaRice_i][_yr]
chaPeasA = obj['AreaH_FAO'][china_i][chaPeas_i][_yr]
chaSugaA = obj['AreaH_FAO'][china_i][chaSuga_i][_yr]
chaMushA = obj['AreaH_FAO'][china_i][chaMush_i][_yr]

print("China total population: ", obj['Popu_FAO'][china_i][_yr])
print()
print("Rice NYield      : ", chaRiceNYield)
print("Peas NYield      : ", chaPeasNYield)
print("Sugar Cane NYield: ", chaSugaNYield)
print("Mushroom NYield  : ", chaMushNYield)
print()
print("Rice Nfer       : ", chaRiceNfer)
print("Peas Nfer       : ", chaPeasNfer)
print("Sugar Cane NYfer: ", chaSugaNfer)
print("Mushroom Nfer   : ", chaMushNfer)
print()
print("Rice Nman      : ", chaRiceNman)
print("Peas Nman      : ", chaPeasNman)
print("Sugar Cane Nman: ", chaSugaNman)
print("Mushroom Nman  : ", chaMushNman)
print()
print("Rice Ndep      : ", chaRiceNdep)
print("Peas Ndep      : ", chaPeasNdep)
print("Sugar Cane Ndep: ", chaSugaNdep)
print("Mushroom Ndep  : ", chaMushNdep)
print()
print("Rice NUE      : ", chaRiceNUE)
print("Peas NUE      : ", chaPeasNUE)
print("Sugar Cane NUE: ", chaSugaNUE)
print("Mushroom NUE  : ", chaMushNUE)
print()
print("Rice Nexc      : ", chaRiceNexc)
print("Peas Nexc      : ", chaPeasNexc)
print("Sugar Cane Nexc: ", chaSugaNexc)
print("Mushroom Nexc  : ", chaMushNexc)
print()
print("Rice Yield      : ", chaRiceY)
print("Peas Yield      : ", chaPeasY)
print("Sugar Cane Yield: ", chaSugaY)
print("Mushroom Yield  : ", chaMushY)
print()
print("Rice Area Harvested      : ", chaRiceA)
print("Peas Area Harvested      : ", chaPeasA)
print("Sugar Cane Area Harvested: ", chaSugaA)
print("Mushroom Area Harvested  : ", chaMushA)
print()

