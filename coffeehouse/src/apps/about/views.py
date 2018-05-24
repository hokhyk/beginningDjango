from django.shortcuts import render

# Create your views here.


def contact(request):
    # Content from request or database extracted here
    # and passed to the template for display
    return render(request, 'about/contact.html')


def index(request):
    # Content from request or database extracted here
    # and passed to the template for display
    return render(request, 'about.html')
