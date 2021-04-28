from country import Country


from catalogue import CountryCatalogue


import os


def processUpdates(cntryFileName, updateFileName):
    # test to see if country file inputted exists or not
    output = open("output.txt", "w")
    while True:
        try:
            file = open(cntryFileName, "r")
            break
        except:
            quit_option = input("Country data file not found. Would you like to quit? Press y for yes or n for no: ")
            # if user quits
            if quit_option.lower() != "n":
                output.write("Update Unsuccessful\n")
                output.close()
                return False
            # if user doesn't quit
            elif quit_option.lower() == "n":
                while True:
                    cntryFileName = input("Please enter new data file name: ")
                    try:
                        file = open(cntryFileName, "r")
                        if file is not None:
                            break
                    except:
                        quit_option2 = input(
                            "Country data file not found. Would you like to quit? Press y for yes or y for no: ")
                        # if user quits
                        if quit_option2.lower() != "n":
                            output.write("Update Unsuccessful\n")
                            output.close()
                            return False
                        # if user doesn't quit, continue on the loop and ask again
                        elif quit_option2.lower() == "n":
                            continue

    output = open("output.txt", "w")
    # test to see if the update file inputted exists or not
    while True:
        try:
            updatefile = open(updateFileName, "r")
            break
        except:
            update_quit_option = input(
                "Country update file not found. Would you like to quit? Press y for yes or n for no: ")
            # if user quits
            if update_quit_option.lower() != "n":
                if os.stat("output.txt").st_size == 0:
                    output.write("Update Unsuccessful\n")
                output.close()
                return False
            # if user doesn't quit
            elif update_quit_option.lower() == "n":
                while True:
                    updateFileName = input("Please enter new update file name: ")
                    try:
                        updatefile = open(updateFileName, "r")
                        if updatefile is not None:
                            break
                    except:
                        update_quit_option2 = input(
                            "Country update file not found. Would you like to quit? Press y for yes or n for no: ")
                        # if user quits
                        if update_quit_option2.lower() != "n":
                            if os.stat("output.txt").st_size == 0:
                                output.write("Update Unsuccessful\n")
                            output.close()
                            return False
                        # if user doesn't quit, continue on the loop and ask again
                        elif update_quit_option2.lower() == "n":
                            continue

    # create an object with countrycatalogue class
    country = CountryCatalogue(cntryFileName)
    for i in updatefile:
        i = i.strip()
        updates = i.split(";")
        # collect corresponding data after splitting line by semicolon
        country1 = Country(updates[0], "", "", "")
        country_object = country.findCountry(country1)
        if country_object is None:
            for x in updates[1:]:
                x = x.strip()
                # check which value that the number corresponds to
                if x[0] == "P":
                    country1.setPopulation(x[2:])
                elif x[0] == "C":
                    country1.setContinent(x[2:])
                elif x[0] == "A":
                    country1.setArea(x[2:])

            # add the country to the catalogue
            country.addCountry(country1.getName(), country1.getPopulation(), country1.getArea(), country1.getContinent())

        else:
            for x in updates[1:]:
                x = x.strip()
                # check which value that the number corresponds to
                if x[0] == "P":
                    country.setPopulationOfCountry(country1, x[2:])
                elif x[0] == "C":
                    country.setContinentOfCountry(country1, x[2:])
                elif x[0] == "A":
                    country.setAreaOfCountry(country1, x[2:])

    # close the file
    file.close()
    # save the file
    country.saveCountryCatalogue("output.txt")
    return True
