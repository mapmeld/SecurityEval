def evalInput(inputStr):
    '''
    run the inputStr as a python expression and return the result
    '''
#    print inputStr
    try:
        return eval(inputStr)
    except:
        return inputStr

def get