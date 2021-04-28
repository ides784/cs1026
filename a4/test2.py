from catalogue import CountryCatalogue


from country import Country


def processUpdates(cntryFileName, updateFileName):
    output = open("output.txt", "w")
    # test to see if the files inputted exist or not
    while True:
        try:
            file = open(cntryFileName, "r")
            break
        except:
            quit_option = input("Data file not found. Would you like to quit? Press Y for yes or N for no: ")
            if quit_option.lower() != "n":
                output.write("Update Unsuccessful\n")
                output.close()
                return False
            elif quit_option.lower() == "n":
                while True:
                    cntryFileName = input("Enter the name of a new data file: ")
                    try:
                        file = open(cntryFileName, "r")
                        if file != None:
                            break
                    except:
                        quit_option2 = input("One or more of your files could not be found. Would you like to quit? Press Y for yes or N for no: ")
                        if quit_option2.lower() != "n":
                            output.write("Update Unsuccessful\n")
                            output.close()
                            return False
                        elif quit_option2.lower() == "n":
                            continue
    # Create an object to the CountryCatalogue class
    country = CountryCatalogue(cntryFileName)
    # Open the update file
    updatefile = open(updateFileName, "r")
    for i in updatefile:
        # String lines
        i = i.strip()
        # Split the data at semicoloumn
        data = i.split(';')
        # Create country object
        cntry1 = Country(data[0], '', '', '')
        # Find country for existence
        obj = country.findCountry(cntry1)
        if obj == None:
            # Fetch values
            for elem in data[1:]:
                # Strip spaces
                elem = elem.strip()
                # Check update
                if elem[0] == 'P':
                    cntry1.setPopulation(elem[2:])
                elif elem[0] == 'A':
                    cntry1.setArea(elem[2:])
                elif elem[0] == 'C':
                    cntry1.setContinent(elem[2:])
            # Add country to catalogue
            country.addCountry(cntry1.getName(), cntry1.getPopulation(), cntry1.getArea(), cntry1.getContinent())
        else:
            for elem in data[1:]:
                # Strip spaces
                elem = elem.strip()
                # Check update
                if elem[0] == 'P':
                    country.setPopulationOfCountry(cntry1, elem[2:])
                elif elem[0] == 'A':
                    country.setAreaOfCountry(cntry1, elem[2:])
                elif elem[0] == 'C':
                    country.setContinentOfCountry(cntry1, elem[2:])
    # Close the file
    file.close()
    # Saving to file
    country.saveCountryCatalogue("output.txt")
    return True