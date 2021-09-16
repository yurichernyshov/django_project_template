from django.shortcuts import render

# Create your views here.

def view_index(request):

    if request.method == 'POST':
        return render(request, 'data.html')
    else:
        return render(request, 'index.html')

