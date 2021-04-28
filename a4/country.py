class Country:
    def __init__(self, name, population, area, continent):
        self.name = name
        self.population = population
        self.area = area
        # error handling if the update file has continent names with incorrect capitalization or too many spaces
        continent = continent.lower()
        continent = continent.split()
        for i, word in enumerate(continent):
            continent[i] = word[0].upper() + word[1:]
        continent = " ".join(continent)
        self.continent = continent

    # define setpopulation function
    def setPopulation(self, p):
        self.population = p

    # define setarea function
    def setArea(self, a):
        self.area = a

    # define setcontinent function
    def setContinent(self, c):
        self.continent = c

    # define setname function
    def getName(self):
        return self.name

    # define setpop function
    def getPopulation(self):
        return self.population

    # define getarea function
    def getArea(self):
        return self.area

    # define getcontinent function
    def getContinent(self):
        return self.continent

    # define representation function
    def __repr__(self):
        return repr(str(self.name)+" (pop: "+str(self.population)+", size: "+str(self.area)+") in "+str(self.continent))
