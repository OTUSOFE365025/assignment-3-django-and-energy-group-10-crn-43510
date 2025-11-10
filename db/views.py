from django.shortcuts import render
from .models import Product
from .forms import ScanForm

def scan_view(request):
    form = ScanForm(request.POST or None)
    product = None
    error = None

    if request.method == "POST" and form.is_valid():
        upc = form.cleaned_data["upc"].strip()
        try:
            product = Product.objects.get(upc=upc)
        except Product.DoesNotExist:
            error = "No product found for that UPC."

    return render(request, "scan.html", {"form": form, "product": product, "error": error})
