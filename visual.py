import scipy
import scipy.io
import numpy as np
#import pandas as pd
#import matplotlib
#import matplotlib.pyplot as plt

DATA = scipy.io.loadmat("iFarmData(2015)_1_28_2019.mat")

#### Example country index finding.
#
#  chaInd = int(np.where(DATA['FAOSTAT_CoName_FAO'] == "China")[0])
usaInd = int(np.where(DATA['FAOSTAT_CoName_FAO'] == "United States of America")[0])

#### Example crop index finding.
#
#  chaRiceInd = int(np.where(DATA['FAOSTAT_CrName_FAO'] == "Rice; paddy")[0])
#  usaRiceInd = int(np.where(DATA['FAOSTAT_CrName_FAO'] == "Rice; paddy")[0])

#### Example data graphing using matplotlib.
#   
#   plt.plot(x values, y values, options)
#   plt.xlabel('insert x label') 
#   plt.ylabel('insert y label')
#   plt.title('insert title')
#   plt.xticks(options) -- options for axis intervals
#   plt.legend(['insert', 'insert '])
#   plt.show()
#   
#   plt.savefig(filename, options); -- save graph to file

#   plt.plot(range(1,len(obj['Yr'][0,:])+1), obj['Nfer_kgkm'][39, 133, :])
#   
#               -all years (indicated by colon), -'Nfer_kgkm' [39 = china, 133 = rice, : = all data related])
#
#   adding another plot will plot on same one before calling show
#   
#   plt.xlabel('Years')
#   plt.ylabel('kgkmg^2 of N')
#   plt.title('N in china for each year')
#   plt.xticks(range(1,len(obj['Yr'][0,:])+1), obj['Yr'][0,:], rotation=80)
#   plt.show()

numCos = max(DATA['FAOSTAT_CoName_FAO'].shape)
numCrops = max(DATA['FAOSTAT_CrName_FAO'].shape)

#### Plots the Nexc variable by country.

#for i in range(numCos): 
#    for j in range(numCrops): 
#        plt.plot(range(1,len(DATA['Yr'][0,:])+1), DATA['Nexc_kgkm'][i, j, :])
#    countryName = DATA['FAOSTAT_CoName_FAO'][i][0][0]
#    plt.title('N pollution crop per year') 
#    plt.xlabel('Years')
#    plt.ylabel('kg/km^2 of N')
#   
#    plt.xticks(range(1,len(DATA['Yr'][0,:])+1), DATA['Yr'][0,:], rotation=90)
#    plt.savefig(f"research/Nexc_graphs/{countryName}.png")
#    plt.clf();


#### Finds max crop N pollution of all countries in all years.
polluted = DATA['Nexc_kgkm'] 
#yr = 0
#while yr < 55:
#    for i in range(numCos):        
#        max_Nexc = np.nanmax(polluted[i, :, yr])
#        filename = "research/Max_Pollution_Stats/%s.txt" % (yr+1961)
#        with open(filename, "a") as f:
#            if np.isnan(max_Nexc):
#                s = "Skipping country " + str(i) + " from nan error\n"
#                f.write(s)
#                continue
#            else:
#                country = DATA['FAOSTAT_CoName_FAO'][i][0][0]
#                max_index = np.where(polluted[i, :, yr] == max_Nexc)
#                s = "The max N pollution in " + country + " in " + str(yr+1961) + " is " + str(DATA['FAOSTAT_CrName_FAO'][max_index[0]][0][0]) + "with " + str("{:.2f}".format(max_Nexc)) + " kg/km." + "\n"
#                f.write(s) 
#    
#    yr = yr + 1

#### Finds min crop N pollution of all countries in all years.

#yr = 0
#while yr < 55:
#    for i in range(numCos):        
#        min_Nexc = np.nanmin(polluted[i, :, yr])
#        filename = "research/Min_Pollution_Stats/%s.txt" % (yr+1961)
#        with open(filename, "a") as f:
#            if np.isnan(min_Nexc):
#                s = "Skipping country " + str(i) + " from nan error\n"
#                f.write(s)
#                continue
#            else:
#                country = DATA['FAOSTAT_CoName_FAO'][i][0][0]
#                min_index = np.where(polluted[i, :, yr] == min_Nexc)
#                s = "The min N pollution in " + country + " in " + str(yr+1961) + " is " + str(DATA['FAOSTAT_CrName_FAO'][min_index[0]][0][0]) + "with " + str("{:.2f}".format(min_Nexc)) + " kg/km." + "\n"
#               f.write(s)

#    yr = yr + 1

dict_crops_max_C = {}
dict_crops_min_C = {}

dict_crops_max = {}
dict_crops_min = {}

Cmin_total = 0
Cmax_total = 0
min_total = 0
max_total = 0
Total_N_pol = 0

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0

#all countries - max
yr = 0
while yr < 55:
    for i in range(numCos):
        max_Nexc = np.nanmax(polluted[i,:,yr])
        if np.isnan(max_Nexc):
            continue
        else:
            country = DATA['FAOSTAT_CoName_FAO'][i][0][0]
            Total_N_pol = Total_N_pol + max_Nexc
            max_index = np.where(polluted[i,:,yr] == max_Nexc)
            c = DATA['FAOSTAT_CrName_FAO'][max_index[0]][0][0][0]
            dict_crops_max[c] = dict_crops_max[c]+1 if c in dict_crops_max else 1
            max_total = max_total+1
            if c == "Sugar cane":
                one = one + max_Nexc
            elif c == "Maize":
                two = two + max_Nexc
            elif c == "Rice; paddy":
                three = three + max_Nexc
            elif c == "Peas; green":
                four = four + max_Nexc
            elif c == "Bananas":
                five = five + max_Nexc
            elif c == "Groundnuts; with shell":
                six = six + max_Nexc
            elif c == "Sugar beet":
                seven = seven + max_Nexc
            elif c == "Beans; green":
                eight = eight + max_Nexc
            elif c == "Wheat":
                nine = nine + max_Nexc
            elif c == "Fruit Fresh Nes":
                ten = ten + max_Nexc
    yr = yr + 1

print ("Total pollution: ", Total_N_pol)
print()
print("Max crops")
print()
print("Sugar cane: ", one)
print("Sugar cane %: ", 100*one/Total_N_pol)
print("Maize: ", two)
print("Maize %: ", 100*two/Total_N_pol)
print("Rice: ", three)
print("Rice %: ", 100*three/Total_N_pol)
print("Peas: ", four)
print("Peas %: ", 100*four/Total_N_pol)
print("Bananas: ", five)
print("Bananas %: ", 100*five/Total_N_pol)
print("Groundnuts: ", six)
print("Groundnuts %: ", 100*six/Total_N_pol)
print("Sugar beets: ", seven)
print("Sugar beets %: ", 100*seven/Total_N_pol)
print("Beans green: ", eight)
print("Beans green %: ", 100*eight/Total_N_pol)
print("Wheat: ", nine)
print("Wheat %: ", 100*nine/Total_N_pol)
print("Fruit Fresh nes: ", ten)
print("Fruit Fresh nes: ", 100*ten/Total_N_pol)

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0


#all countries - min
yr = 0
while yr < 55:
    for i in range(numCos):
        min_Nexc = np.nanmin(polluted[i,:,yr])
        if np.isnan(min_Nexc):
            continue
        else:
            min_index = np.where(polluted[i,:,yr] == min_Nexc)
            c = DATA['FAOSTAT_CrName_FAO'][min_index[0]][0][0][0]
            dict_crops_min[c] = dict_crops_min[c]+1 if c in dict_crops_min else 1
            min_total = min_total+1
            if c == "Tobacco; unmanufactured":
                one = one + min_Nexc
            elif c == "Cabbages and other brassicas":
                two = two + min_Nexc
            elif c == "Spices; nes":
                three = three + min_Nexc
            elif c == "Potatoes":
                four = four + min_Nexc
            elif c == "Oil palm fruit":
                five = five + min_Nexc
            elif c == "Garlic":
                six = six + min_Nexc
            elif c == "Mushrooms and truffles":
                seven = seven + min_Nexc
            elif c == "Ginger":
                eight = eight + min_Nexc
            elif c == "Roots and Tubers; nes":
                nine = nine + min_Nexc
            elif c == "Seed cotton":
                ten = ten + min_Nexc
    yr = yr + 1
print()
print("Min crops")
print()
print("Tobacco: ", one)
print("Tobacco %: ", 100*one/Total_N_pol)
print("Cabbages: ", two)
print("Cabbages %: ", 100*two/Total_N_pol)
print("Spices: ", three)
print("Spices %: ", 100*three/Total_N_pol)
print("Potatoes: ", four)
print("Potatoes %: ", 100*four/Total_N_pol)
print("Oil palm fruit: ", five)
print("Oil palm fruit %: ", 100*five/Total_N_pol)
print("Garlic: ", six)
print("Garlic %: ", 100*six/Total_N_pol)
print("Mushrooms: ", seven)
print("Mushrooms %: ", 100*seven/Total_N_pol)
print("Ginger: ", eight)
print("Ginger %: ", 100*eight/Total_N_pol)
print("Roots: ", nine)
print("Roots %: ", 100*nine/Total_N_pol)
print("Seed cotton: ", ten)
print("Seed cotton %: ", 100*ten/Total_N_pol)


#just china dictionary stuff-max
yr = 0
C_Total_N_pol = 0
Peas = 0
SC = 0
Van = 0
while yr < 55:
    max_Nexc = np.nanmax(polluted[39,:,yr])
    if np.isnan(max_Nexc):
        continue
    else:
        C_Total_N_pol = C_Total_N_pol + max_Nexc
        max_index = np.where(polluted[39,:,yr] == max_Nexc)
        c = DATA['FAOSTAT_CrName_FAO'][max_index[0]][0][0][0]
        dict_crops_max_C[c] = dict_crops_max_C[c]+1 if c in dict_crops_max_C else 1
        Cmax_total = Cmax_total+1
        if c == "Peas; green":
            Peas = Peas + max_Nexc
        elif c == "Sugar cane":
            SC = SC + max_Nexc
        elif c == "Vanilla":
            Van = Van + max_Nexc

    yr=yr+1
print("China stats:")
print("------------")
print("Total China N pollution: ", C_Total_N_pol)
print()
print("Max Crops")
print()
print("Peas: ", Peas)
print("Peas %: ", 100*Peas/C_Total_N_pol)
print("Sugar cane: ", SC)
print("Sugar cane %: ", 100*SC/C_Total_N_pol)
print("Vanilla: ", Van)
print("Vanilla %: ", 100*Van/C_Total_N_pol)

#just china dictionary stuff-min
yr = 0
Mush = 0
Spic = 0
while yr < 55:
    min_Nexc = np.nanmin(polluted[39,:,yr])
    if np.isnan(min_Nexc):
        continue
    else:
        min_index = np.where(polluted[39,:,yr] == min_Nexc)
        c = DATA['FAOSTAT_CrName_FAO'][min_index[0]][0][0][0]
        dict_crops_min_C[c] = dict_crops_min_C[c]+1 if c in dict_crops_min_C else 1
        Cmin_total = Cmin_total+1
        if c == "Mushrooms and truffles":
            Mush = Mush + min_Nexc
        elif c == "Spices; nes":
            Spic = Spic + min_Nexc
    yr=yr+1
print("Min Crops")
print()
print("Mushrooms: ", Mush)
print("Mushrooms %: ", 100*Mush/C_Total_N_pol)
print("Spices: ", Spic)
print("Spices %: ", 100*Spic/C_Total_N_pol)

yr = 0
USA_Total_N_pol = 0
Peas = 0
while yr < 55:
    max_Nexc = np.nanmax(polluted[usaInd,:,yr])
    if np.isnan(max_Nexc):
        continue
    else:
        USA_Total_N_pol = USA_Total_N_pol + max_Nexc
        max_index = np.where(polluted[usaInd,:,yr] == max_Nexc)
        c = DATA['FAOSTAT_CrName_FAO'][max_index[0]][0][0][0]
        if c == "Peas; green":
            Peas = Peas + max_Nexc
    yr=yr+1

yr = 0
Ginger = 0
Tobac = 0
while yr < 55:
    min_Nexc = np.nanmin(polluted[usaInd,:,yr])
    if np.isnan(min_Nexc):
        continue
    else:
        min_index = np.where(polluted[usaInd,:,yr] == min_Nexc)
        c = DATA['FAOSTAT_CrName_FAO'][min_index[0]][0][0][0]
        if c == "Ginger":
            Ginger = Ginger + min_Nexc
        elif c == "Tobacco; unmanufactured":
            Tobac = Tobac + min_Nexc
    yr=yr+1


print("USA stats")
print("---------")
print("USA total N pol: ", USA_Total_N_pol)
print()
print("Max Crops")
print()
print("Peas: ", Peas)
print("Peas %: ", 100*Peas/USA_Total_N_pol)
print()
print("Min Crops")
print()
print("Ginger: ", Ginger)
print("Ginger %: ", 100*Ginger/USA_Total_N_pol)
print("Tobacco: ", Tobac)
print("Tobacco %: ", 100*Tobac/USA_Total_N_pol)
