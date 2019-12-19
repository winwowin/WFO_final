from django.contrib import admin
from .models import Supplier, Product, Part, Assembling, Product_coordinator, Coordinator, Tier

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Part)
admin.site.register(Assembling)
admin.site.register(Product_coordinator)
admin.site.register(Coordinator)
admin.site.register(Tier)
