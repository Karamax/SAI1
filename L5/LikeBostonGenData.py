import random
# Заменить на словарь
crimMin = 0.00632
znMin = 0
indusMin = 0.46
chasMin = 0
noxMin = 0.385
rmMin = 3.561
ageMin = 2.9
disMin = 1.1296
radMin = 1
taxMin = 187
ptratioMin = 12.6
blackMin = 0.32
lstatMin = 1.73
medvMin = 5

crimMax = 88.9762
znMax = 100
indusMax = 27.74
chasMax = 1
noxMax = 0.871
rmMax = 8.78
ageMax = 100
disMax = 12.1265
radMax = 24
taxMax = 711
ptratioMax = 22
blackMax = 396.9
lstatMax = 37.97
medvMax = 50

count = int(input('Enter rows count: '))

rows = ',"crim","zn","indus","chas","nox","rm","age","dis","rad","tax","ptratio","black","lstat","medv"'+'\n'

for i in range(count): # Заменит на цикл
    row = str(round(random.uniform(crimMin, crimMax),5))+','+str(round(random.uniform(znMin, znMax),1))+','\
    +str(round(random.uniform(indusMin, indusMax),2))+','+str(random.randint(chasMin, chasMax))+','\
    +str(round(random.uniform(noxMin, noxMax),3))+','+str(round(random.uniform(rmMin, rmMax),3))+','\
    +str(round(random.uniform(ageMin, ageMax),1))+','+str(round(random.uniform(disMin, disMax),4))+','\
    +str(random.randint(radMin, radMax))+','+str(random.randint(taxMin, taxMax))+','\
    +str(round(random.uniform(ptratioMin, ptratioMax),1))+','+str(round(random.uniform(blackMin, blackMax),1))\
    +','+str(round(random.uniform(lstatMin, lstatMax),2))+','+str(round(random.uniform(medvMin, medvMax),1))+'\n'
    rows +=  row
file = open('out.csv', 'w')
file.write(rows)
file.close()
