from django.shortcuts import render
from .utils import dede

# Create your views here.
def index(request):
    print("Index view called")
    return render(request, 'index.html')

def scrape_material_view(request):
    if request.method == 'POST':
        print("Scrape view called")
        material_name = request.POST.get('material_name')

        # Call the scraper function for example.com
        products = dede(material_name)

        # Pass the results to the template
        return render(request, 'index.html', {'products': products,'material_name': material_name})

    return render(request, 'index.html')
