from tempfile import mktemp

def write_results(results):
    '''
    create a temporary file and write the results to it
    '''
#    print "writing results to file"
    with open(results, 'w') as f: