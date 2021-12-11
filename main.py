import pandas as pd

pd.options.display.max_columns = 9
pd.set_option('display.width', 1400)

with open('guns.txt', encoding="utf8") as gunsfile:
    guns = []
    guns = gunsfile.readlines()
    guns = [line.rstrip('\n') for line in guns]

print("Зброя:",*guns,sep="\n")
print("\n")

with open('parameters.txt', encoding="utf8") as fileparameters:
    parameters = []
    parameters = fileparameters.readlines()
    parameters = [line.rstrip('\n') for line in parameters]

print("Параметри:",*parameters,sep="\n")
print("\n")
print("Шкала оцінювання: 1-5")
print("\n")

with open('importance.txt', encoding="utf8") as fileimportance:
    importance = []
    importance = fileimportance.readlines()
    importance = [line.rstrip('\n') for line in importance]

file1 = open ('1.txt' , 'r')
exp1 = []
exp1 = [ line.split() for line in file1]

file2 = open ('2.txt' , 'r')
exp2 = []
exp2 = [ line.split() for line in file2]

file3 = open ('3.txt' , 'r')
exp3 = []
exp3 = [ line.split() for line in file3]

file4 = open ('4.txt' , 'r')
exp4 = []
exp4 = [ line.split() for line in file4]

def Price (gun):
    price = float(importance[0]) * (float(exp1[gun][0])+float(exp2[gun][0])+float(exp3[gun][0])+float(exp4[gun][0]))
    return price

def Barrel (gun):
    display = float(importance[1]) * (float(exp1[gun][1])+float(exp2[gun][1])+float(exp3[gun][1])+float(exp4[gun][1]))
    return display

def Caliber (gun):
    caliber = float(importance[2]) * (float(exp1[gun][2])+float(exp2[gun][2])+float(exp3[gun][2])+float(exp4[gun][2]))
    return caliber

def Capacity (gun):
    capacity = float(importance[3]) * (float(exp1[gun][3])+float(exp2[gun][3])+float(exp3[gun][3])+float(exp4[gun][3]))
    return capacity

def Weight (gun):
    weight = float(importance[4]) * (float(exp1[gun][4])+float(exp2[gun][4])+float(exp3[gun][4])+float(exp4[gun][4]))
    return weight

def Comfort (gun):
    comfort = float(importance[5]) * (float(exp1[gun][5])+float(exp2[gun][5])+float(exp3[gun][5])+float(exp4[gun][5]))
    return comfort

def Lenght (gun):
    lenght = float(importance[6]) * (float(exp1[gun][6])+float(exp2[gun][6])+float(exp3[gun][6])+float(exp4[gun][6]))
    return lenght

#Daniel Defense DDM4 V7 PRO
priceDDM4 = Price(0)
barrelDDM4 = Barrel(0)
caliberDDM4 = Caliber(0)
capacityDDM4 = Capacity(0)
weightDDM4 = Weight(0)
comfortDDM4 = Comfort(0)
lenghtDDM4 = Lenght(0)

#FN SCAR 16S
priceScar = Price(1)
barrelScar = Barrel(1)
caliberScar = Caliber(1)
capacityScar = Capacity(1)
weightScar = Weight(1)
comfortScar = Comfort(1)
lenghtScar = Lenght(1)

#KelTec 308Win
priceKel = Price(2)
barrelKel = Barrel(2)
caliberKel = Caliber(2)
capacityKel = Capacity(2)
weightKel = Weight(2)
comfortKel = Comfort(2)
lenghtKel = Lenght(2)

#МКМ-072
priceMkm = Price(3)
barrelMkm = Barrel(3)
caliberMkm = Caliber(3)
capacityMkm = Capacity(3)
weightMkm = Weight(3)
comfortMkm = Comfort(3)
lenghtMkm = Lenght(3)

#Форт-229М
priceFort = Price(4)
barrelFort = Barrel(4)
claiberFort = Caliber(4)
capacityFort = Capacity(4)
weightFort = Weight(4)
comfortFort = Comfort(4)
lenghtFort = Lenght(4)

#Сума
sumDDM4 = priceDDM4 + caliberDDM4 + barrelDDM4 + comfortDDM4 + weightDDM4 + lenghtDDM4 + capacityDDM4
sumScar = priceScar + caliberScar + barrelScar + comfortScar + weightScar + lenghtScar + capacityScar
sumKel = priceKel + caliberKel + barrelKel + comfortKel + weightKel + lenghtKel + capacityKel
sumMkm = priceMkm + caliberMkm + barrelMkm + comfortMkm + weightMkm + lenghtMkm + capacityMkm
sumFort= priceFort + claiberFort + barrelFort + comfortFort + weightFort + lenghtFort + capacityFort

parameters.append('')
importance.append('')

df = pd.DataFrame({'№': ['1', '2', '3', '4', '5', '6', '7', 'Сума'],
                   'Параметри': parameters,
                   'Вага': importance,
                   guns[0]: [priceDDM4, barrelDDM4, caliberDDM4, capacityDDM4, weightDDM4, comfortDDM4, lenghtDDM4, sumDDM4],
                   guns[1]: [priceScar, barrelScar, caliberScar, capacityScar, weightScar, comfortScar, lenghtScar, sumScar],
                   guns[2]: [priceKel, barrelKel, caliberKel, capacityKel, weightKel, comfortKel, lenghtKel, sumKel],
                   guns[3]: [priceMkm, barrelMkm, caliberMkm, capacityMkm, weightMkm, comfortMkm, lenghtMkm, sumMkm],
                   guns[4]: [priceFort, barrelFort, claiberFort, capacityFort, weightFort, comfortFort, lenghtFort, sumFort]})

print("Результат:")
print(df)
print('\n')

winner = ''
points = ''

if sumDDM4 > sumFort and sumDDM4 > sumKel and sumDDM4 > sumScar and sumDDM4 > sumMkm:
    winner = guns[0]
    points = sumDDM4
elif sumScar > sumFort and sumScar > sumKel and sumScar > sumDDM4 and sumScar > sumMkm:
    winner = guns[1]
    points = sumScar
elif sumKel > sumFort and sumKel > sumScar and sumKel > sumDDM4 and sumKel > sumMkm:
    winner = guns[2]
    points = sumKel
elif sumMkm > sumFort and sumMkm > sumScar and sumMkm > sumDDM4 and sumMkm > sumKel:
    winner = guns[3]
    points = sumMkm
elif sumFort > sumMkm and sumFort > sumScar and sumFort > sumDDM4 and sumFort > sumKel:
    winner = guns[4]
    points = sumFort
else:
    print("Помилка, або переможець не один!")

print("Найкращій варіант:",winner, '-', points)
print('\n')