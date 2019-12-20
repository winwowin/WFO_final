from django.contrib import admin
from .models import Supplier, Product, Part, Assembling, Product_coordinator, Coordinator, Tier, Address, Country, \
    State, Billing

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Part)
admin.site.register(Assembling)
admin.site.register(Product_coordinator)
admin.site.register(Coordinator)
admin.site.register(Tier)
# admin.site.register(Address)
# admin.site.register(Country)
# admin.site.register(State)
# admin.site.register(Billing)
