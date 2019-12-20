from django.shortcuts import redirect


def redirect_root_view(request):
    return redirect('companyinfo2_product_list_urlpattern')
