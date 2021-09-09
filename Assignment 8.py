
# Assignment 8.py

# CSC 110 Section 03
# Romero J.H. Hutapea
# November 21, 2019

# This program reads data from a file and shows a report to the user.
# The data are specifically for the world GDP data.
# Each line in the file contains data that formatted as:
# name of country, population, GDP

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main():
    fileName = getInput()
    infile = openFile(fileName)
    lineContent = processFile(infile) # This is a list
    numberCountry = countCountry(lineContent)
    totalPop = totalPopulation(lineContent)
    highestPop, hiPopCountry = hiPopulation(lineContent)
    lowestPop, lowPopCountry = lowPopulation(lineContent)
    highestGDP, hiGDPCountry = hiGDP(lineContent)
    lowestGDP, lowGDPCountry = lowGDP(lineContent)
    listOfCapita = listCapita(lineContent) # This is a list of country + their Capita
    worldCapita = totalCapita(listOfCapita)
    worldAverageCapita = averageCapita(worldCapita, numberCountry)
    richCountry, poorCountry = richPoorCountry(worldAverageCapita, listOfCapita)
    highestCapita, hiCapitaCountry = hiCapitaGDP(listOfCapita)
    lowestCapita, lowCapitaCountry = lowCapitaGDP(listOfCapita)
    print()
    print('There are a total of ' + str(numberCountry) + ' Countries.')
    print('World total populaton: ' + format(totalPop, ',.0f') + ' people.')
    print()
    print('Country with Highest population: ' + str(hiPopCountry) \
          + ' with ' + format(highestPop, ',.0f') + ' people.')
    print('Country wiith Lowest population: ' + str(lowPopCountry)\
          + ' with ' + format(lowestPop, ',.0f') + ' people.')
    print()
    print('Country with Highest GDP: ' + str(hiGDPCountry)\
          + ' with ' + format(highestGDP, ',.2f') + ' GDP.')
    print('Country with Lowest GDP: ' + str(lowGDPCountry)\
          + ' with ' + format(lowestGDP, ',.2f') + ' GDP.')
    print()
    print('Country with Highest GDP per CAPITA: ' + str(hiCapitaCountry)\
          + ' with ' + format(highestCapita, ',.2f') + ' GDP per CAPITA.')
    print('Country with Lowest GDP per CAPITA: ' + str(lowCapitaCountry)\
          + ' with ' + format(lowestCapita, ',.2f') + ' GDP per CAPITA.')
    print()
    print('World average GDP per CAPITA: ' + format(worldAverageCapita, ',.2f'))
    print()
    outputList(poorCountry, richCountry)

# Getting user input
def getInput():
    fileName = input('What is your file name? :')
    return fileName

# Open the file
def openFile(fileName):
    openThis = open(fileName + '.txt','r')
    return openThis

# Read and process file
def processFile(infile):
    read = infile.readline()
    #   content = ''
    lineContent = []
    while read != '':
        strippedRead = read.rstrip()
        lineContent.append(strippedRead.split(','))
    #    content += strippedRead + '\n'

        read = infile.readline()
    #print(content) 
    return lineContent # Return 2 dimensional list
    infile.close()
    
# Find the total amount of country
def countCountry(lineContent):
    country = 0
    for data in range(len(lineContent)):
        country += 1
    return country

# Find total population
def totalPopulation(lineContent):
    population = 0
    for data in range(len(lineContent)):
        for index in range(len(lineContent[data])):
            if index == 1:
                population += int(lineContent[data][index])
    return population

# Find a country with highest population
# Return highest population with its country
def hiPopulation(lineContent):
    high = int(lineContent[0][1])
    country = ''
    for data in range(len(lineContent)):
        for index in range(len(lineContent[data])):
            if index == 1:
                if int(lineContent[data][index]) > high:
                    country = (lineContent[data][index-1])
                    high = int(lineContent[data][index])
    return high, country

# Find a country with lowest population
def lowPopulation(lineContent):
    low = int(lineContent[0][1])
    country = ''
    for data in range(len(lineContent)):
        for index in range(len(lineContent[data])):
            if index == 1:
                if int(lineContent[data][index]) < low:
                    country = (lineContent[data][index-1])
                    low = int(lineContent[data][index])
    return low, country

# Find a country with a highest GDP
def hiGDP(lineContent):
    high = int(lineContent[0][2])
    country = (lineContent[0][0])
    for data in range(len(lineContent)):
        for index in range(len(lineContent[data])):
            if index == 2:
                if int(lineContent[data][index]) > high:
                    country = (lineContent[data][index-2])
                    high = int(lineContent[data][index])
    return high, country

# Find a country with a lowest GDP
def lowGDP(lineContent):
    low = int(lineContent[0][2])
    country = (lineContent[0][0])
    for data in range(len(lineContent)):
        for index in range(len(lineContent[data])):
            if index == 2:
                if int(lineContent[data][index]) < low:
                    country = (lineContent[data][index-2])
                    low = int(lineContent[data][index])
    return low, country

# Finding the GDP per capita in each country
# and append it to a list
# Return a list
def listCapita(lineContent):
    listCapita = []
    for data in range(len(lineContent)):
        dataEachCountry = []
        for index in range(len(lineContent[data])):
            if index == 0:
                country = (lineContent[data][index])
                dataEachCountry.append(country)
            elif index == 1:
                population = int(lineContent[data][index])
            elif index == 2:
                GDP = int(lineContent[data][index])
        countryCapita = GDP / population
        dataEachCountry.append(countryCapita)
        listCapita.append(dataEachCountry)
    return listCapita

# Find a country with a highest GDP per capita
def hiCapitaGDP(listCapita):
    high = listCapita[0][1]
    country = listCapita[0][0]
    for data in range(len(listCapita)):
        for index in range(len(listCapita[data])):
            if index == 1:
                nextValue = listCapita[data][index]
                if nextValue > high:
                    high = listCapita[data][index]
                    country = listCapita[data][0]
    return high, country

# Find a country with a lowest GDP per capita
def lowCapitaGDP(listCapita):
    low = listCapita[0][1]
    country = listCapita[0][0]
    for data in range(len(listCapita)):
        for index in range(len(listCapita[data])):
            if index == 1:
                nextValue = listCapita[data][index]
                if nextValue < low:
                    low = listCapita[data][index]
                    country = listCapita[data][0]
    return low, country

# Find the total GDP per capita of all nation
def totalCapita(lineContent):
    totalCapita = 0
    for data in range(len(lineContent)):
        for index in range(len(lineContent[data])):
            if index == 1:
                eachCapita = float(lineContent[data][index])
                totalCapita += eachCapita
                
    return totalCapita

# Find the average GDP per capita of all nation
def averageCapita(worldCapita, numberCountry):
    averageCapita = worldCapita / numberCountry
    return averageCapita
                
# Find the rich and poor country
# return the list of rich country and poor country
def richPoorCountry(averageCapita, listCapita):
    richThreshold = averageCapita * 3       # 300 %
    poorThreshold = averageCapita * 0.025   # 97.5 %
    richCountry = []
    poorCountry = []
  
    for data in range(len(listCapita)):
        temporaryString = ''
        isRich = False
        isPoor = False
        for index in range(len(listCapita[data])):
            if index == 0:
                country = (listCapita[data][index])
                temporaryString += country
            elif index == 1:
                countryCapita = listCapita[data][index]
                # temporaryList.append(countryCapita)
                if countryCapita > richThreshold:
                    isRich = True
                elif countryCapita < poorThreshold:
                    isPoor = True
        if isPoor:
            poorCountry.append(listCapita[data])
        elif isRich:
            richCountry.append(listCapita[data])
    
    return richCountry, poorCountry

def outputList(poorList, richList):
    print('Rich Country:\n')
    for index in range(len(richList)):
        print(richList[index][0].ljust(35) + '$' + format(richList[index][1], ',.2f'))
    print()
    print('Poor Country:\n')
    for index in range(len(poorList)):
        print(poorList[index][0].ljust(35) + '$' + format(poorList[index][1], ',.2f'))
    print()
 
main()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Documented test cases
# Sample:
# wakanda,1,10000000000
# usa,100,100000
# china,40000,120000000
# brazil,500,120000
#
# Output:
# There are a total of 4 Countries.
# World total populaton: 40,601 people.
#
# Country with Highest population: china with 40,000 people.
# Country wiith Lowest population:  with 1 people.
#
# Country with Highest GDP: wakanda with 10,000,000,000.00 GDP.
# Country with Lowest GDP: usa with 100,000.00 GDP.
#
# Country with Highest GDP per CAPITA: wakanda with 10,000,000,000.00 GDP per CAPITA.
# Country with Lowest GDP per CAPITA: brazil with 240.00 GDP per CAPITA.
#
# World average GDP per CAPITA: 2,500,001,060.00
#
# Rich Country:
#
# wakanda                            $10,000,000,000.00
#
# Poor Country:
#
# usa                                $1,000.00
# china                              $3,000.00
# brazil                             $240.00

