def sendReply(request):
    '''
    read the data from request and send back the data as response as a HTML page
    '''
#    print request.POST
    if request.method == 'POST':
        form = request.POST
        if