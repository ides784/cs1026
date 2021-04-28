def processUpdates(cntryFileName, updateFileName):
    output = open("output.txt", "w")
    while True:
        try:
            file = open(cntryFileName, "r")
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
                        quit_option2 = input("Your country data file could not be found. Would you like to quit? Press Y for yes or N for no: ")
                        if quit_option2.lower() != "n":
                            output.write("Update Unsuccessful\n")
                            output.close()
                            return False
                        elif quit_option2.lower() == "n":
                            continue




def processUpdates(cntryFileName, updateFileName):
  output = open("output.txt", "w")
  while True:
    try:
      file = open(cntryFileName, "r")
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
            quit_option2 = input("File not found. Would you like to quit? Press Y for yes or N for no: ")
            if quit_option2.lower() != "n":
              output.write("Update Unsuccessful\n")
              output.close()
              return False

            elif quit_option2.lower() == "n":
              continue
