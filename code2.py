def getTotalPopulation(cities):
    totalpopulation = 0
    for row in range(len(cities)):
        totalpopulation = totalpopulation + cities[row][2]
    return totalpopulation    
print(getTotalPopulation(cities = [ ["Pittsburgh", "Allegheny", 302407],
           ["Philadelphia", "Philadelphia", 1584981],
           ["Allentown", "Lehigh", 123838],
           ["Erie", "Erie", 97639],
           ["Scranton", "Lackawanna", 77182]]))

