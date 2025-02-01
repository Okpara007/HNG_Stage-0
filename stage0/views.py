from django.http import HttpResponse

def homepage(request):
    return HttpResponse('<h1>Welcome! Please go to <a href="/api">/api</a> to access the API.</h1>')
