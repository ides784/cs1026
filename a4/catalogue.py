from country import Country


class CountryCatalogue:

    def __init__(self, countryFile):
        # create and open country information list
        self.countryCat = []
        country = open(countryFile, "r")
        country.readline()
        # read each line from the country file, then iterate
        for x in country:
            x = x.strip()
            data = x.split('|')
            # split data accordingly
            x = Country(data[0], data[2], data[3], data[1])
            self.countryCat.append(x)
        country.close()

    def setContinentOfCountry(self, country, continent):
        for x in range(len(self.countryCat)):
            if self.countryCat[x].getName() == country.getName():
                self.countryCat[x].setContinent(continent)

    def setAreaOfCountry(self, country, area):
        for x in range(len(self.countryCat)):
            if self.countryCat[x].getName() == country.getName():
                self.countryCat[x].setArea(area)

    def setPopulationOfCountry(self, country, population):
        for x in range(len(self.countryCat)):
            if self.countryCat[x].getName() == country.getName():
                self.countryCat[x].setPopulation(population)

    def findCountry(self, country):
        # iterate over all countries
        for x in self.countryCat:
            if x.getName() == country.getName():
                return country
            else:
                return None

    def addCountry(self, countryName, pop, area, cont):
        # iterate over every country
        repeats = False
        for x in range(len(self.countryCat)):
            if self.countryCat[x].getName() == countryName:
                repeats = True
        if repeats is True:
            return False
        else:
            y = Country(countryName, pop, area, cont)
            self.countryCat.append(y)
            return True

    def printCountryCatalogue(self):
        # print using defined format
        for x in self.countryCat:
            print(repr(x))

    def saveCountryCatalogue(self, fname):
        # sort list
        sorted_catalogue = sorted(self.countryCat, key=(lambda country: country.getName()))
        file = open(fname, "w")
        # create a header
        file.write("Country|Continent|Population|Area\n")
        items_written = 0
        # iterate every item according the required format
        for x in sorted_catalogue:
            file.write(x.getName() + "|" + x.getContinent() + "|" + x.getPopulation() + "|" + x.getArea() + "\n")
            items_written = items_written + 1
        file.close()
        # success scenario
        if items_written == len(self.countryCat):
            return items_written
        # failed scenario
        else:
            return -1