import process
# ====================================================================================================================== #
# Title: customValueX                                                                                                    #
# Description:                                                                                                           #
#       This function is called when user have chosen to change the value of X (in the previous operation). This asks    #
#   for the values for both X and Y (function of X) and displays the inputs.                                             #
# ====================================================================================================================== #
def customValueX(n):
    xv = []         # list for the x values
    fx = []         # list for the f(x) values

    tRange = n

    for i in range(tRange):
        xvIn = float(input("Enter x{}:    ".format(i)))
        xv.append(xvIn)
        fxIn = float(input("Enter fx{}:   ".format(i)))
        fx.append(fxIn)

    print("\n")
    print("""========== ORDERED PAIRS ==========
          x      f(x)        """)
    for i in range(tRange):
        print("         ({} , ".format(xv[i])+ "{})".format(fx[i]))

    process.dataPointsOpt(tRange, xv, fx)
    return

# ====================================================================================================================== #
# Title: defaultValueX                                                                                                   #
# Description:                                                                                                           #
#       This function is called when user have chosen to not change the value of X (in the previous operation). This     #
#   asks for the values for Y (function of X) and displays the inputs.                                                   #
# ====================================================================================================================== #
def defaultValueX(n):
    xv = []         # list for the x values
    fx = []         # list for the f(x) values

    tRange = n

    for i in range(int(tRange)):
    
        fxIn = float(input("Enter fx{}: ".format(i)))
        fx.append(fxIn)
        xv.append(i)

    print("\n")
    print("""========== ORDERED PAIRS ==========
          x   f(x)        """)
    for i in range(tRange):
        print("         ({}, ".format(i)+ "{})".format(fx[i]))
 
    process.dataPointsOpt(tRange, xv, fx)
    return