def convert_to_int():
    '''
    take an input from user and convert it to int within a try-except block
    '''
#    try:
#        return int(input())
    except ValueError:
        return input()

