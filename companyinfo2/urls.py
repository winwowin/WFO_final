# from django.urls import path, include
#
# from companyinfo2.views import (
#     assembling_list_view,
#     product_list_view,
#     supplier_list_view,
#     part_list_view,
#     coordinator_list_view,
#     product_coordinator_list_view,
# )
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('assembling/', assembling_list_view),
#     path('product/', product_list_view),
#     path('supplier/', supplier_list_view),
#     path('part/', part_list_view),
#     path('coordinator/', coordinator_list_view),
#     path('product_coordinator/', product_coordinator_list_view),
# ]

from django.urls import path

from .views import (
    AssemblingList,
    ProductList,
    PartList,
    SupplierList,
    CoordinatorList,
    Product_coordinatorList,
    AssemblingDetail,
    ProductDetail,
    PartDetail,
    SupplierDetail,
    CoordinatorDetail,
    Product_coordinatorDetail)

urlpatterns = [

    path('assembling/',
         AssemblingList.as_view(),
         name='companyinfo_assembling_list_urlpattern'),

    path('assembling/<int:pk>/',
        AssemblingDetail.as_view(),
        name='companyinfo_assembling_detail_urlpattern'),

    path('product/',
         ProductList.as_view(),
         name='companyinfo_product_list_urlpattern'),

    path('product/<int:pk>/',
        ProductDetail.as_view(),
        name='companyinfo_product_detail_urlpattern'),

    path('part/',
         PartList.as_view(),
         name='companyinfo_part_list_urlpattern'),

    path('part/<int:pk>/',
        PartDetail.as_view(),
        name='companyinfo_part_detail_urlpattern'),

    path('supplier/<int:pk>/',
        SupplierDetail.as_view(),
        name='companyinfo_supplier_detail_urlpattern'),

    path('supplier/',
         SupplierList.as_view(),
         name='companyinfo_supplier_list_urlpattern'),

    path('coordinator/',
         CoordinatorList.as_view(),
         name='companyinfo_coordinator_list_urlpattern'),

    path('coordinator/<int:pk>/',
        CoordinatorDetail.as_view(),
        name='companyinfo_coordinator_detail_urlpattern'),

    path('product_coordinator/',
         Product_coordinatorList.as_view(),
         name='companyinfo_product_coordinator_list_urlpattern'),

    path('product_coordinator/<int:pk>/',
         Product_coordinatorDetail.as_view(),
         name='companyinfo_product_coordinator_detail_urlpattern'),

]












from django.urls import path

from .views import (
    AssemblingList,
    ProductList,
    PartList,
    SupplierList,
    CoordinatorList,
    Product_coordinatorList,
    AssemblingDetail,
    ProductDetail,
    PartDetail,
    SupplierDetail,
    CoordinatorDetail,
    Product_coordinatorDetail,
    AssemblingCreate,
    AssemblingUpdate,
    AssemblingDelete,
    ProductCreate,
    ProductUpdate,
    ProductDelete,
    PartCreate,
    PartUpdate,
    PartDelete,
    SupplierCreate,
    SupplierUpdate,
    SupplierDelete,
    CoordinatorCreate,
    CoordinatorUpdate,
    CoordinatorDelete,
    Product_coordinatorCreate,
    Product_coordinatorUpdate,
    Product_coordinatorDelete,
)

urlpatterns = [

    path('assembling/',
         AssemblingList.as_view(),
         name='companyinfo_assembling_list_urlpattern'),

    path('assembling/<int:pk>/',
        AssemblingDetail.as_view(),
        name='companyinfo_assembling_detail_urlpattern'),

    path('assembling/create/',
         AssemblingCreate.as_view(),
         name='companyinfo_assembling_create_urlpattern'),

    path('assembling/<int:pk>/update/',
         AssemblingUpdate.as_view(),
         name='companyinfo_assembling_update_urlpattern'),

    path('assembling/<int:pk>/delete/',
         AssemblingDelete.as_view(),
         name='companyinfo_assembling_delete_urlpattern'),

    path('product/',
         ProductList.as_view(),
         name='companyinfo_product_list_urlpattern'),

    path('product/<int:pk>/',
        ProductDetail.as_view(),
        name='companyinfo_product_detail_urlpattern'),

    path('product/create/',
         ProductCreate.as_view(),
         name='companyinfo_product_create_urlpattern'),

    path('product/<int:pk>/update/',
         ProductUpdate.as_view(),
         name='companyinfo_product_update_urlpattern'),

    path('product/<int:pk>/delete/',
         ProductDelete.as_view(),
         name='companyinfo_product_delete_urlpattern'),

    path('part/',
         PartList.as_view(),
         name='companyinfo_part_list_urlpattern'),

    path('part/<int:pk>/',
        PartDetail.as_view(),
        name='companyinfo_part_detail_urlpattern'),

    path('part/create/',
         PartCreate.as_view(),
         name='companyinfo_part_create_urlpattern'),

    path('part/<int:pk>/update/',
         PartUpdate.as_view(),
         name='companyinfo_part_update_urlpattern'),

    path('part/<int:pk>/delete/',
         PartDelete.as_view(),
         name='companyinfo_part_delete_urlpattern'),

    path('supplier/<int:pk>/',
        SupplierDetail.as_view(),
        name='companyinfo_supplier_detail_urlpattern'),

    path('supplier/',
         SupplierList.as_view(),
         name='companyinfo_supplier_list_urlpattern'),

    path('supplier/create/',
         SupplierCreate.as_view(),
         name='companyinfo_supplier_create_urlpattern'),

    path('supplier/<int:pk>/update/',
         SupplierUpdate.as_view(),
         name='companyinfo_supplier_update_urlpattern'),

    path('supplier/<int:pk>/delete/',
         SupplierDelete.as_view(),
         name='companyinfo_supplier_delete_urlpattern'),

    path('coordinator/',
         CoordinatorList.as_view(),
         name='companyinfo_coordinator_list_urlpattern'),

    path('coordinator/<int:pk>/',
        CoordinatorDetail.as_view(),
        name='companyinfo_coordinator_detail_urlpattern'),

    path('coordinator/create/',
         CoordinatorCreate.as_view(),
         name='companyinfo_coordinator_create_urlpattern'),

    path('coordinator/<int:pk>/update/',
         CoordinatorUpdate.as_view(),
         name='companyinfo_coordinator_update_urlpattern'),

    path('coordinator/<int:pk>/delete/',
         CoordinatorDelete.as_view(),
         name='companyinfo_coordinator_delete_urlpattern'),

    path('product_coordinator/',
         Product_coordinatorList.as_view(),
         name='companyinfo_product_coordinator_list_urlpattern'),

    path('product_coordinator/<int:pk>/',
         Product_coordinatorDetail.as_view(),
         name='companyinfo_product_coordinator_detail_urlpattern'),

    path('product_coordinator/create/',
         Product_coordinatorCreate.as_view(),
         name='companyinfo_product_coordinator_create_urlpattern'),

    path('product_coordinator/<int:pk>/update/',
         Product_coordinatorUpdate.as_view(),
         name='companyinfo_product_coordinator_update_urlpattern'),

    path('product_coordinator/<int:pk>/delete/',
         Product_coordinatorDelete.as_view(),
         name='companyinfo_product_coordinator_delete_urlpattern'),

]
