from django.http import HttpResponseRedirect, HttpResponse

def set_location_header(request):
    '''
    get url data from the request and set the location header for redirecting
    '''
	if request.method == 'POST':
	    location_