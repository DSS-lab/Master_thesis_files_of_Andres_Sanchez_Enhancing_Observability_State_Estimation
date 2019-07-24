###############################################################################
#Three different options  of functions to evaluate the error of the state     #
#estimation procedure and be able to validate the method. The 1st one finds   #
#the different between the estimated values and the validation set of         #
#measurements. The 2nd one corresponds to the percentual relative error of the#
#estimated values and the validation set of measurements. tHE 3rd one is the  #
#absolute error in per unit base. Run only the section that corresponds to the#
#desired error calculation.                                                   #
###############################################################################

def Calc_Error(Estimated, Validation):
    Error=Estimated-Validation
    return Error

def Calc_Error(Estimated, Validation):
    Error=100*abs((Estimated-Validation)/Validation)
    return Error

def Calc_Error(Estimated, Validation, PU_Base):
    Error=(Estimated-Validation)/PU_Base
    return Error