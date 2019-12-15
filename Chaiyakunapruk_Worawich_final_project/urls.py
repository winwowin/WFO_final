from django.contrib import admin
from django.urls import path

from companyinfo.views import (
    assembling_list_view,
    product_list_view,
    supplier_list_view,
    part_list_view,
    coordinator_list_view,
    product_coordinator_list_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('assembling/', assembling_list_view),
    path('product/', product_list_view),
    path('supplier/', supplier_list_view),
    path('part/', part_list_view),
    path('coordinator/', coordinator_list_view),
    path('product_coordinator/', product_coordinator_list_view),
]
