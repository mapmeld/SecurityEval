from django.http import HttpResponseRedirect

def http_responser_redirect(request):
    '''
    get the target url from the request and redirect to it
    '''
#    if request.method == 'POST':
#        form = http