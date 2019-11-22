import math
import csv
import random
from copy import deepcopy
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

#Some hints on how to start have been added to this file.
#You will have to add more code that just the hints provided here for the full implementation.


# ====
# Define a function that computes the distance between two data points
def dataDistance(a, b, ax=1):
    return np.linalg.norm(a-b, axis=ax)


# ====
# Define a function that reads data in from the csv files  HINT: http://docs.python.org/2/library/csv.html
def readCsv(file):
    dataSet = []
    countries = []
    birthRate = []
    lifeExp = []
    
    with open(file) as csvfile:
        read = csv.reader(csvfile)
        #Skips the first row
        next(read)
        for row in read:
            dataSet.append(row)
            countries.append(row[0])
            birthRate.append(row[1])
            lifeExp.append(row[2])
           
        return countries, dataSet, birthRate, lifeExp

# ====
# Write the initialisation procedure
countries, dataSet, birthRate, lifeExp = readCsv('databoth.csv')


#All data:
#Converts array elements to type float
a = np.asarray(birthRate, dtype=float)
b = np.asarray(lifeExp, dtype=float)

allData = np.array(list(zip(a, b)))

#Requests how mnay clusters the user would like
numClusters = int(input("How many clusters would you like: "))
print()


#Centroid data:
cent_X = random.sample(birthRate, numClusters)
cent_Y = random.sample(lifeExp, numClusters)

#Converts sample array elements into type float
x = np.asarray(cent_X, dtype=float)
y = np.asarray(cent_Y, dtype=float)


#Centroid*
centroids = np.array(list(zip(x, y)))


#Placeholder for the previous centroids
oldCentroids = np.zeros(centroids.shape)
#print(oldCentroids)


#Cluster labels
clusterLabels = np.zeros(len(allData))


#Distance between the old and the new centroids
distance = dataDistance(centroids, oldCentroids, None)


# ====
# Implement the k-means algorithm, using appropriate looping
while(distance != 0):
    for i in range(len(allData)):
        #Assign data to closest centroid 
        assignCluster = dataDistance(allData[i], centroids)
        #What is np.argmin?
        cluster = np.argmin(assignCluster)
        clusterLabels[i] = cluster

    oldCentroids = deepcopy(centroids)

    #Finds new centroids
    for j in range(numClusters):
        points = [allData[k] for k in range(len(allData)) if clusterLabels[k] == j]
        centroids[j] = np.mean(points, axis=0)
    distance = dataDistance(centroids, oldCentroids, None)
    #print(distance)


# ====
# Print out the results
#Question 1:
    
#Gets the elements for each cluster
elementsPerCluster={i: np.where(clusterLabels == i)[0] for i in range(numClusters)}
for elements in range(numClusters):
    print("The number of elements in cluster {} is {}".format(elements,len(elementsPerCluster[elements])))
print()

#Question 2:

#Get the countries grouped to each cluster
countryDict = {}
for cd in range(len(countries)):
    countryAssign = {cd: countries[cd]}
    countryDict.update(countryAssign)


for i in range(numClusters):
    clust = elementsPerCluster[i]

    for j in range(len(clust)):
            print("Cluster {0}, Country: {1}".format(i, countryDict.get(clust[j])))
print()

#Question 3:
#Calculate the mean of the birth rate and life expectancy for each cluster
meanDict = {}
for md in range(len(allData)):
        meanAssign = {md: allData[md]}
        meanDict.update(meanAssign)

#print(meanDict)
for i in range(numClusters):
    clust = elementsPerCluster[i]

    for j in range(len(clust)):
        meanBirthArray = meanDict.get(clust[j])[0]
        lifeExpArray = meanDict.get(clust[j])[1]
        #Calculate means
        meanBMean = np.mean(meanBirthArray)
        lifeEMean = np.mean(lifeExpArray)
    print("Cluster {0} Mean Birthrate: {1} Mean life Expectancy: {2}".format(i, meanBMean, lifeEMean))
    
    
##Plot scatterplots
colors = ['r', 'g', 'b', 'y', 'c', 'm']
fig, ax = plt.subplots()
for i in range(numClusters):
        points = np.array([allData[j] for j in range(len(allData)) if clusterLabels[j] == i])
        ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
ax.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, c='#050505')
plt.show()



#*******************************************************************************************
#Compare clusters to determine which countries have move to different clusters for 4 clusters

#Seperate all clusters into seperate lists
    
#List for first cluster
clust0 = []
List1 = []

for i in range(len(elementsPerCluster[0])):
    clust0.append(elementsPerCluster[0][i])


for j in clust0:
    List1.append(countryDict.get(j))

#List for second cluster
clust1 = []
List2 = []

for i in range(len(elementsPerCluster[1])):
    clust1.append(elementsPerCluster[1][i])


for j in clust1:
    List2.append(countryDict.get(j))


#List for the third cluster
clust2 = []
List3 = []

for i in range(len(elementsPerCluster[2])):
    clust2.append(elementsPerCluster[2][i])


for j in clust2:
    List3.append(countryDict.get(j))


#List for the fourth cluster
#List for the third cluster
clust3 = []
List4 = []

for i in range(len(elementsPerCluster[3])):
    clust3.append(elementsPerCluster[3][i])


for j in clust3:
    List4.append(countryDict.get(j))


#***************************************************************************************
#List that will be used for comaprisons

#First comparator list
realList1 = []
for l1 in List1:
    realList1.append(l1[6:])


#Second comparator list
realList2 = []
for l2 in List2:
    realList2.append(l2[6:])


#Third comparator list
realList3 = []
for l3 in List3:
    realList3.append(l3[6:])


#Fourth comparator list
realList4 = []
for l4 in List4:
    realList4.append(l4[6:])


#Comparing lists
def compare(list1, list2, list3, list4):
    a=[]
    for i in list1:
        if i in list2:
            a.append(i)
        if i in list3:
            a.append(i)
        if i in list4:
            a.append(i)
    for j in list2:
        if j in list3:
            a.append(j)
        if j in list4:
            a.append(j)
    for k in list3:
        if k in list4:
            a.append(k)
    return a

print()
print("All the countries that have moved clusters are: ")
print()
print(compare(realList1, realList2, realList3, realList4))
