import scipy
import scipy.io
import numpy as np
import pandas as pd
#print(f"China N for rice in 2010: {obj['Nfer_kgkm'][39][133][49]}.")
#
#Separates the data in obj to separate files by name of variable
#Don't need to rerun
#
#for i in obj.keys():
#    if i[0] != '_':
#        np.save(i,obj[i])
#
#FAOSTAT_CoName_FAO = np.load('FAOSTAT_CoName_FAO.npy',allow_pickle=True)
#FAOSTAT_CrName_FAO = np.load('FAOSTAT_CrName_FAO.npy',allow_pickle=True)
#Yr = np.load('Yr.npy',allow_pickle=True)
#pd.set_option("display.max_rows", None, "display.max_column", None)


#------------------------------------------------------------------------

###
##
#        Load in data
##
###
obj = scipy.io.loadmat("iFarmData(2015)_1_28_2019.mat")
###
##
#        Easy to use variables for the following problems.
##
###

chaInd = int(np.where(obj['FAOSTAT_CoName_FAO'] == "China")[0])
riceInd = int(np.where(obj['FAOSTAT_CrName_FAO'] == "Rice; paddy")[0])
###
##
#        Find the years' index in the data file.
##
###
yr1986 = int(np.where(obj['Yr'][0] == 1986)[0]) 
yr2010 = int(np.where(obj['Yr'][0] == 2010)[0])
yr2011 = int(np.where(obj['Yr'][0] == 2011)[0])
yr2015 = int(np.where(obj['Yr'][0] == 2015)[0])
###
##
#        Number of countries and crops to analyze.
##
###

numCos = max(obj['FAOSTAT_CoName_FAO'].shape)
numCrops = max(obj['FAOSTAT_CrName_FAO'].shape)
numTrdYrs = yr2015 - yr1986 

#############
###
##
#
#        Formula = Ninput = Nfer + Nman + Nfix + Ndep
#        Nsur = Ninput - nyield
#        NUE = Nyield/Ninput
#
##
###
##
#        China 2010 Statistics
##
###
chaRiceNYield2010 = obj['Nyield_kgkm'][chaInd, riceInd, yr2010]

chaRiceNInput2010 = np.nansum([obj['Nfer_kgkm'][chaInd, riceInd, yr2010], obj['Nman_kgkm'][chaInd, riceInd, yr2010],
                            obj['Nfix_kgkm'][chaInd, riceInd, yr2010], obj['Ndep_kgkm'][chaInd, riceInd, yr2010]])
print(f"Input = ")
print(chaRiceNInput2010)

print(f"Yield = ")
print(chaRiceNYield2010)
chaRiceNSur2010 = chaRiceNInput2010 - chaRiceNYield2010
print(f"Surplus = ")
print(chaRiceNSur2010)

NUE2010 = chaRiceNYield2010/chaRiceNInput2010
print(f"NUE = ")
print(NUE2010)

###########
###
##
#        Global Nsur,co,yr = (sum cr (Nsur,co,cr,yr * Aco,cr,yr))/sum cr Aco,cr,yr
#        NUEco,yr = (sum cr (Nyield,co,cr,yr * Aco,cr,yr))/(sum cr Ninput,co,cr,yr * Aco,cr,yr)
##
###
###########

globeCropIn = obj['Nfer_kgkm'] + obj['Nman_kgkm'] + obj['Nfix_kgkm'] + obj['Ndep_kgkm']
globeCropSur = globeCropIn - obj['Nyield_kgkm']

print(f"globeCropIn =")
print(globeCropIn)

print(f"globeCropSure =")
print(globeCropSur)

##########
###
##
#       All Countries, All Crops, All Years, Agg by Crops
##
###
##########

globalCropAGG = np.reshape(np.nansum(globeCropSur*(obj['AreaH_FAO']),axis=1) / np.nansum(obj['AreaH_FAO'], axis=1), newshape=[numCos, max(obj['Yr'].shape)])
globalCropNUE = np.reshape(np.nansum(obj['Nyield_kgkm']*obj['AreaH_FAO'],axis=1) / np.nansum(globeCropIn*obj['AreaH_FAO'],axis=1), newshape=[numCos, max(obj['Yr'].shape)])
print(f"globalCropAGG: ")
print(globalCropAGG)
print(f"globalCropNUE: ")
print(globalCropNUE)

##########
###
##
#       How much N has China been importing?
#       Amount of N in traded crops
##
###
##########

tradeN = np.empty((obj['netImTrade'].shape)) #creates empty array of size of netImTrade max(shape) - length, size - shape
print(f"tradeN")
print(tradeN)

for i in range(max(obj['NC_Bou'].shape)):
    tradeN[i,:,:,:] = obj['netImTrade'][i,:,:,:] * obj['NC_Bou'][0,i]

print(f"tradeN filled: ")
print(tradeN)

##########
###
##
#       Net N input to China
##
###
##########

#netNIm_China = np.nansum(np.reshape(tradeN[:,:,chaInd,:], newshape=[numCrops,numTrdYrs,numCos]),axis=2)

##########
###
##
#       Aggregate by crops
##
###
##########

#agNIm_China = np.nansum(netNIm_China, axis = 0)

##########
###
##
#       Amount of N pollution if China did not import
#       Amount of N surplus China would have produced without trade
##
###
##########

#chinaNUE = np.reshape(obj['NUE_3d'][chaInd,:,yr1986:yr2015,[numCrops,numTrdYrs])
#notImN_China = ((1/chinaNUE)-1)*netNIm_China
#agNotImN_China = np.nansum(notImN_China), axis=0)

