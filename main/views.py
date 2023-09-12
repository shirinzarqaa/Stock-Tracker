from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Shirin Zarqaa Rabbaanii Arham',
        'class': 'PBP F',
        'application' : 'StockTracker'
    }

    return render(request, "main.html", context)