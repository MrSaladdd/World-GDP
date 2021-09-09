
# Assignment 8.py

# CSC 110 Section 03
# Romero J.H. Hutapea
# November 21, 2019

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
    highestCapita, hiCapitaCountry = hiCapitaGDP(lineContent)
    lowestCapita, lowCapitaCountry = lowCapitaGDP(lineContent)
    listedCapita = listCapita(lineContent) # This is a list of country + their Capita
    worldCapita = totalCapita(listedCapita)
    worldAverageCapita = averageCapita(worldCapita, numberCountry)
    richCountry, poorCountry = richPoorCountry(worldAverageCapita, listedCapita)
##    cont, am = hihi(listedCapita)
##    print(lineContent)
##    print(numberCountry)
##    print(totalPop)
##    print(hiPopCountry, highestPop)
##    print(lowPopCountry, lowestPop)
##    print()
##    print(hiGDPCountry, highestGDP)
##    print(lowGDPCountry, lowestGDP)
##    print(hiCapitaCountry, highestCapita)
##    print(lowCapitaCountry, lowestCapita)
##    print(worldCapita)
    print(worldAverageCapita)
    print(listedCapita)
    print()
    print('rich =', richCountry)
    print()
    print('poor =', poorCountry)
##    print(cont, am)
    
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
    content = ''
    lineContent = []
    while read != '':
        strippedRead = read.rstrip()
        lineContent.append(strippedRead.split(','))
        content += strippedRead + '\n'
        
        #print(strippedRead)
        read = infile.readline()
    
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
                    high = int(lineContent[data][index])
    return high, country

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

# Find a country with a highest GDP per capita
def hiCapitaGDP(lineContent):
    population = int(lineContent[0][1])
    GDP = int(lineContent[0][2])
    country = (lineContent[0][0])
    high = GDP / population
    for data in range(len(lineContent)):
        for index in range(len(lineContent[data])):
            if index == 1:
                population = int(lineContent[data][index])
            elif index == 2:
                GDP = int(lineContent[data][index])
                
            capitaGDP = GDP / population
            
            if capitaGDP > high:
                high = capitaGDP
                if index == 2:
                    country = (lineContent[data][index-2])
    return high, country

# Find a country with a lowest GDP per capita
def lowCapitaGDP(lineContent):
    population = int(lineContent[0][1])
    GDP = int(lineContent[0][2])
    country = (lineContent[0][0])
    low = GDP / population
    for data in range(len(lineContent)):
        for index in range(len(lineContent[data])):
            if index == 1:
                population = int(lineContent[data][index])
            elif index == 2:
                GDP = int(lineContent[data][index]) 
            capitaGDP = GDP / population
            if capitaGDP < low:
                low = capitaGDP
                if index == 0:
                    country = (lineContent[data][index])
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

# Finding highest GDP capita
# another method
##def hihi(listCapita):
##    high = float(listCapita[0][1])
##    country = (listCapita[0][0])
##    for data in range(len(listCapita)):
##        for index in range(len(listCapita[data])):
##            if index == 1:
##                if listCapita[data][index] > high:
##                    high = listCapita[data][index]
##                    country = listCapita[data][index-1]
##    return high, country

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
def richPoorCountry(averageCapita, listCapita):
    richThreshold = averageCapita * 3       # 300 %
    poorThreshold = averageCapita * 0.975   # 97.5 %
    richCountry = []
    poorCountry = []
    
    for data in range(len(listCapita)):
        temporaryList = []
        isRich = False
        isPoor = False
        for index in range(len(listCapita[data])):
            if index == 0:
                country = (listCapita[data][index])
                temporaryList.append(country)
            elif index == 1:
                countryCapita = listCapita[data][index]
                # temporaryList.append(countryCapita)
                if countryCapita > richThreshold:
                    isRich = True
                elif countryCapita < poorThreshold:
                    isPoor = True
        if isPoor:
            poorCountry.append(temporaryList)
        elif isRich:
            richCountry.append(temporaryList)
    return richCountry, poorCountry
            
                
                
            
                
    
        
    














    

    
main()
