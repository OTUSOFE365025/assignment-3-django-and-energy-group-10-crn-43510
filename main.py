############################################################################
## Django ORM Standalone Python Template
############################################################################
import sys
sys.dont_write_bytecode = True

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

import django
django.setup()

from db.models import Product   # ✅ Import your Product model

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

# Show all products loaded from fixtures
print("=== Available Products ===")
for p in Product.objects.all():
    print(f"{p.upc} — {p.name} — ${p.price}")

# Simple scan loop
while True:
    upc = input("\nEnter product UPC (or 'q' to quit): ").strip()
    if upc.lower() == 'q':
        print("Exiting Cash Register.")
        break

    try:
        product = Product.objects.get(upc=upc)
        print(f"✅ Product Found: {product.name} — ${product.price}")
    except Product.DoesNotExist:
        print("❌ Product not found. Try again.")
