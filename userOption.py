import valueOfX
# ====================================================================================================================== #
# Title: askForOption                                                                                                    #
# Description:                                                                                                           #
#       This function asks user whether they want to change the values of X and the asks for the range of values they    #
#   want to be interpolated - extrapolated.                                                                              #
# ====================================================================================================================== #
def askForOption():
    print("Data Interpolator / Extrapolator!")
    print("""By:              Christian Clyde G. Deciero
                 Allexis Kyth O. Sunit
                 Jude Edrian S. Co
                """)
    opt = input("Do you want to modify the values of X? [Y / N]\nAns:")
    
    while opt != ['Y', 'y'] and opt != ['N', 'n']:

        if opt == 'Y' or opt == 'y':
            print("\n*====================*\n\tWelcome\n*====================*")
            n = int(input("Enter range of the tables: "))
            
            while n <= 1:
                print("Enter 2 or more values.")
                print("\n")
                n = int(input("Enter range of the tables: "))
            else:
                valueOfX.customValueX(n)
            break
            
        elif opt == 'N' or opt == 'n':
            print("\n*====================*\n\tWelcome\n*====================*")
            n = int(input("Enter the range: "))

            while n <= 1:
                print("Enter 2 or more values.")
                print("\n")
                n = int(input("Enter range of the tables: "))
            else:
                valueOfX.defaultValueX(n)
            break

        else:
            print("Invalid entry!")
            opt = input("Do you want to modify the values of X? [Y / N]\nAns:")

    return

