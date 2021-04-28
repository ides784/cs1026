from country import Country

continent = continent.lower()
continent = continent.split()
for i, word in enumerate(continent):
    if word == 'of':
        continent[i] = 'of'
    else:
        continent[i] = word[0].upper() + word[1:]
continent = " ".join(name)

class CountryCatalogue:

    def __init__(self, countryFile):
        # create country information list
        self.countryCat = []
        country = open(countryFile, "r")
        country.readline()
        # read each line from the country file
        for x in country:
            x = x.strip()
            data = x.split('|')
            x = Country(data[0], data[2], data[3], data[1])
            self.countryCat.append(x)
        country.close()

    def setPopulationOfCountry(self, country, population):
        for x in range(len(self.countryCat)):
            if self.countryCat[x].getName() == country.getName():
                self.countryCat[x].setPopulation(population)

    def setAreaOfCountry(self, country, area):
        for x in range(len(self.countryCat)):
            if self.countryCat[x].getName() == country.getName():
                self.countryCat[x].setArea(area)

    def setContinentOfCountry(self, country, continent):
        for x in range(len(self.countryCat)):
            if self.countryCat[x].getName() == country.getName():
                self.countryCat[x].setContinent(continent)

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
        for i in range(len(self.countryCat)):
            if self.countryCat[i].getName() == countryName:
                repeats = True
        if repeats is True:
            return False
        else:
            x = Country(countryName, pop, area, cont)
            self.countryCat.append(x)
            return True

    def printCountryCatalogue(self):
        for i in self.countryCat:
            print(repr(i))

    def saveCountryCatalogue(self, fname):
        # sort list
        sorted_catalogue = sorted(self.countryCat, key=(lambda country: country.getName()))
        file = open(fname, "w")
        # create a header
        file.write("Country|Continent|Population|Area\n")
        items_written = 0
        # iterate every item according the required format
        for i in sorted_catalogue:
            file.write(i.getName() + "|" + i.getContinent() + "|" + i.getPopulation() + "|" + i.getArea() + "\n")
            items_written = items_written + 1
        file.close()
        if items_written == len(self.countryCat):
            return items_written
        else:
            return -1
