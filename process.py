
# ====================================================================================================================== #
# Title: dataPointsOpt                                                                                                   #
# Description:                                                                                                           #
#       This function asks user how many data points they want to use for interpolating - extrapolating.                 #
# ====================================================================================================================== #
def dataPointsOpt(tRange, xv, fx):
    i = 0
   
    print("\n")
    x = float(input("Enter value X:     "))


    for i in range(tRange):
        if float(x) == float (xv[i]):
            ans = fx[i]

            print("Result: f({}) = ".format(x) + "{}" .format(ans))
            break
    else:
        optData = int(input("Enter desired data points: "))

        while optData != [2, 3, 4]:
            if optData == 2 and tRange >= 2:
                print("Utilizing Laplace in 2nd degree...")
                twoDataEntry(x, xv, fx, tRange)
                break

            elif optData == 3 and tRange >= 3:
                print("Utilizing Laplace in 3rd degree...")
                threeDataEntry(x, xv, fx, tRange)
                break
        
            elif optData == 4 and tRange >= 4:
                print("Utilizing Laplace in 4th degree...")
                fourDataEntry(x, xv, fx, tRange)
                break
            
            else:
                print("Invalid entry!\n")
                optData = int(input("Enter desired data points: "))
                

    return

# ====================================================================================================================== #
# Title: twoDataEntry                                                                                                    #
# Description:                                                                                                           #
#       This function is called when user have chosen to use 2 data points.                                              #
# ====================================================================================================================== #
def twoDataEntry(x, xv, fx, tRange):

    xZero = 0
    xOne = 0

    Y0 = 0
    Y1 = 0

    if float(x) < float(xv[0]):
        print("Extrapolating...")
        xZero = xv[0]
        Y0 = fx[0]
        xOne = xv[1]
        Y1 = fx[1]

    elif float(x) > float(xv[tRange-1]):
        print("Extrapolating...")
        xZero = xv[tRange-2]
        Y0 = fx[tRange-2]
        xOne = xv[tRange-1]
        Y1 = fx[tRange-1]

    else:
        print("Interpolating...")
        for i in range(tRange):
            if float(xv[i]) <= float(x):
                xZero = xv[i]
                Y0 = fx[i]

            if float(xv[i]) > float(x):
                xOne = xv[i]
                Y1 = fx[i]
                break

    print("\n--------------------")
    print("x = {}".format(x))
    print("--------------------")

    print("X0 = {}".format(xZero))
    print("--------------------")

    print("X1 = {}".format(xOne))
    print("--------------------")

    print("Y0 = {}".format(Y0))
    print("--------------------")

    print("Y1 = {}".format(Y1))
    print("--------------------\n")

    L1 = (x - xOne) / (xZero - xOne)
    L2 = (x - xZero) / (xOne - xZero)

    appF = ((float(L1) * float(Y0)) + (float(L2) * float(Y1)))
    print("Result: f({}) = ".format(x) + "{}" .format(appF))
    return

# ====================================================================================================================== #
# Title: threeDataEntry                                                                                                  #
# Description:                                                                                                           #
#       This function is called when user have chosen to use 3 data points.                                              #
# ====================================================================================================================== #
def threeDataEntry(x, xv, fx, tRange):
    xZero = 0
    xOne = 0
    xTwo = 0

    Y0 = 0
    Y1 = 0
    Y2 = 0
    
    if float(x) < float(xv[0]):
            print("Extrapolating...")
            xZero = xv[0]
            Y0 = fx[0]
            xOne = xv[1]
            Y1 = fx[1]
            xTwo = xv[2]
            Y2 = fx[2]

    elif float(x) > float(xv[tRange-1]):
            print("Extrapolating...")
            xZero = xv[tRange-3]
            Y0 = fx[tRange-3]
            xOne = xv[tRange-2]
            Y1 = fx[tRange-2]
            xTwo = xv[tRange-1]
            Y2 = fx[tRange-1]
    
    else:
            print("Interpolating...")
            for i in range(tRange):
                if float(xv[i+1]) < float(x):
                    xZero = xv[i]
                    Y0 = fx[i]
                elif float(xv[i]) < float(x):
                    xOne = xv[i]
                    Y1 = fx[i]
                if float(xv[i]) > float(x): 
                    xTwo = xv[i]
                    Y2 = fx[i]
                    break

    print("\n--------------------")
    print("x = {}".format(x))
    print("--------------------")

    print("X0 = {}".format(xZero))
    print("--------------------")

    print("X1 = {}".format(xOne))
    print("--------------------")

    print("X2 = {}".format(xTwo))
    print("--------------------")

    print("Y0 = {}".format(Y0))
    print("--------------------")

    print("Y1 = {}".format(Y1))
    print("--------------------")

    print("Y2 = {}".format(Y2))
    print("--------------------\n")
    
    L0 = ((x - xOne) / (xZero - xOne)) * ((x - xTwo) / (xZero - xTwo)) 
    L1 = ((x - xZero) / (xOne - xZero)) * ((x - xTwo) / (xOne - xTwo)) 
    L2 = ((x - xZero) / (xTwo - xZero)) * ((x - xOne) / (xTwo - xOne))
    appF = (float(L0) * float(Y0) + float(L1) * float(Y1) + float(L2) * float(Y2))
    print("Result: f({}) = ".format(x) + "{}" .format(appF))
    
    return

# ====================================================================================================================== #
# Title: fourDataEntry                                                                                                   #
# Description:                                                                                                           #
#       This function is called when user have chosen to use 4 data points.                                              #
# ====================================================================================================================== #
def fourDataEntry(x, xv, fx, tRange):           
    xZero = 0
    xOne = 0
    xTwo = 0
    xThree = 0

    Y0 = 0
    Y1 = 0
    Y2 = 0  
    Y3 = 0

    if float(x) < float(xv[0]):
            print("Extrapolating...")
            xZero = xv[0]
            Y0 = fx[0]
            xOne = xv[1]
            Y1 = fx[1]
            xTwo = xv[2]
            Y2 = fx[2]
            xThree = xv[3]
            Y3 = fx[3]

    elif float(x) > float(xv[tRange-1]):
            print("Extrapolating...")
            xZero = xv[tRange-4]
            Y0 = fx[tRange-4]
            xOne = xv[tRange-3]
            Y1 = fx[tRange-3]
            xTwo = xv[tRange-2]
            Y2 = fx[tRange-2]
            xThree = xv[tRange-1]
            Y3 = fx[tRange-1]
    
    else:
            print("Interpolating...")
            for i in range(tRange):
                if float(xv[i]) < float(x):
                    xZero = xv[i-1]
                    Y0 = fx[i-1]
                    xOne = xv[i]
                    Y1 = fx[i]
                elif float(xv[i]) > float(x):
                    xTwo = xv[i]
                    Y2 = fx[i]
                    xThree = xv[i+1]
                    Y3 = fx[i+1]
                    break

    print("\n--------------------")
    print("x = {}".format(x))
    print("--------------------")

    print("X0 = {}".format(xZero))
    print("--------------------")

    print("X1 = {}".format(xOne))
    print("--------------------")

    print("X2 = {}".format(xTwo))
    print("--------------------")

    print("X3 = {}".format(xThree))
    print("--------------------")

    print("Y0 = {}".format(Y0))
    print("--------------------")

    print("Y1 = {}".format(Y1))
    print("--------------------")

    print("Y2 = {}".format(Y2))
    print("--------------------")

    print("Y3 = {}".format(Y3))
    print("--------------------\n")
    
    L0 = ((x - xOne) / (xZero - xOne)) * ((x - xTwo) / (xZero - xTwo)) * ((x - xThree) / (xZero - xThree))
    L1 = ((x - xZero) / (xOne - xZero)) * ((x - xTwo) / (xOne - xTwo)) * ((x - xThree) / (xOne - xThree))
    L2 = ((x - xZero) / (xTwo - xZero)) * ((x - xOne) / (xTwo - xOne)) * ((x - xThree) / (xTwo - xThree))
    L3 = ((x - xZero) / (xThree - xZero)) * ((x - xOne)/ (xThree - xOne)) * ((x - xTwo) / (xThree - xTwo)) 
    appF = (float(L0) * float(Y0) + float(L1) * float(Y1) + float(L2) * float(Y2) + float(L3) * float(Y3))
    print("Result: f({}) = ".format(x) + "{}" .format(appF))
    return

