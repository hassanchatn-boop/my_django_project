from django.shortcuts import render

# Create your views here.
def home(request):
    name = {
        'c': 'jhafnfmnf'
    }
    return render(request, 'my_template.html', name)