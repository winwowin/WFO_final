from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from companyinfo2.utils import PageLinksMixin

from django.shortcuts import render, get_object_or_404
from django.views import View

from companyinfo2.forms import AssemblingForm, ProductForm, PartForm, SupplierForm, CoordinatorForm, \
    Product_coordinatorForm


from .models import (
    Assembling,
    Product,
    Part,
    Supplier,
    Coordinator,
    Product_coordinator,
)


class AssemblingList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Assembling


class AssemblingDetail(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'companyinfo2.view_assembling'

    def get(self, request, pk):
        assembling = get_object_or_404(
            Assembling,
            pk=pk
        )
        product_list = assembling.products.all()
        return render(
            request,
            'companyinfo2/assembling_detail.html',
            {'assembling': assembling, 'product_list': product_list}
        )


class AssemblingCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = AssemblingForm
    model = Assembling
    permission_required = 'companyinfo2.add_assembling'


class AssemblingUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = AssemblingForm
    model = Assembling
    template_name = 'companyinfo2/assembling_form_update.html'
    permission_required = 'companyinfo2.change_assembling'
    

class AssemblingDelete(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'companyinfo2.delete_assembling'

    def get(self, request, pk):
        assembling = self.get_object(pk)
        products = assembling.products.all()
        if products.count() > 0:
            return render(
                request,
                'companyinfo2/assembling_refuse_delete.html',
                {'assembling': assembling,
                 'products': products,
                 }
            )
        else:
            return render(
                request,
                'companyinfo2/assembling_confirm_delete.html',
                {'assembling': assembling}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Assembling,
            pk=pk)

    def post(self, request, pk):
        assembling = self.get_object(pk)
        assembling.delete()
        return redirect('companyinfo2_assembling_list_urlpattern')


class ProductList(ListView):
        model = Product


class ProductDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'companyinfo2.view_product'

    def get(self, request, pk):
        product = get_object_or_404(
            Product,
            pk=pk
        )
        supplier = product.supplier
        part = product.part
        assembling = product.assembling
        product_coordinator_list = product.product_coordinators.all()
        return render(
            request,
            'companyinfo2/product_detail.html',
            {'product': product,
             'supplier': supplier,
             'part': part,
             'assembling': assembling,
             'product_coordinator_list': product_coordinator_list}
        )


class ProductCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ProductForm
    model = Product
    permission_required = 'companyinfo2.add_product'


class ProductUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'companyinfo2/product_form_update.html'
    permission_required = 'companyinfo2.change_product'


class ProductDelete(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'companyinfo2.delete_product'

    def get(self, request, pk):
        product = self.get_object(pk)
        product_coordinators = product.product_coordinators.all()
        if product_coordinators.count() > 0:
            return render(
                request,
                'companyinfo2/product_refuse_delete.html',
                {'product': product,
                 'product_coordinators': product_coordinators,
                 }
            )
        else:
            return render(
                request,
                'companyinfo2/product_confirm_delete.html',
                {'product': product}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Product,
            pk=pk)

    def post(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return redirect('companyinfo2_product_list_urlpattern')


class PartList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Part
    permission_required = 'companyinfo2.view_part'


class PartDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'companyinfo2.view_part'

    def get(self, request, pk):
        part = get_object_or_404(
            Part,
            pk=pk
        )
        product_list = part.products.all()
        return render(
            request,
            'companyinfo2/part_detail.html',
            {'part': part, 'product_list': product_list}
        )


class PartCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PartForm
    model = Part
    permission_required = 'companyinfo2.add_part'


class PartUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PartForm
    model = Part
    template_name = 'companyinfo2/part_form_update.html'
    permission_required = 'companyinfo2.change_part'


class PartDelete(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'companyinfo2.delete_part'

    def get(self, request, pk):
        part = self.get_object(pk)
        products = part.products.all()
        if products.count() > 0:
            return render(
                request,
                'companyinfo2/part_refuse_delete.html',
                {'part': part,
                 'products': products,
                 }
            )
        else:
            return render(
                request,
                'companyinfo2/part_confirm_delete.html',
                {'part': part}
            )

    def get_object(self, pk):
        part = get_object_or_404(
            Part,
            pk=pk
        )
        return part

    def post(self, request, pk):
        part = self.get_object(pk)
        part.delete()
        return redirect('companyinfo2_part_list_urlpattern')


class SupplierList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Supplier
    permission_required = 'companyinfo2.view_supplier'


class SupplierDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'companyinfo2.view_supplier'

    def get(self, request, pk):
        supplier = get_object_or_404(
            Supplier,
            pk=pk
        )
        product_list = supplier.products.all()
        return render(
            request,
            'companyinfo2/supplier_detail.html',
            {'supplier': supplier, 'product_list': product_list}
        )


class SupplierCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SupplierForm
    model = Supplier
    permission_required = 'companyinfo2.add_supplier'


class SupplierUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = SupplierForm
    model = Supplier
    template_name = 'companyinfo2/supplier_form_update.html'
    permission_required = 'companyinfo2.change_supplier'


class SupplierDelete(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'companyinfo2.delete_supplier'

    def get(self, request, pk):
        supplier = self.get_object(pk)
        products = supplier.products.all()
        if products.count() > 0:
            return render(
                request,
                'companyinfo2/supplier_refuse_delete.html',
                {'supplier': supplier,
                 'products': products,
                 }
            )
        else:
            return render(
                request,
                'companyinfo2/supplier_confirm_delete.html',
                {'supplier': supplier}
            )

    def get_object(self, pk):
        supplier = get_object_or_404(
            Supplier,
            pk=pk
        )
        return supplier

    def post(self, request, pk):
        supplier = self.get_object(pk)
        supplier.delete()
        return redirect('companyinfo2_supplier_list_urlpattern')


class CoordinatorList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Coordinator
    permission_required = 'companyinfo2.view_coordinator'


class CoordinatorDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'companyinfo2.view_coordinator'

    def get(self, request, pk):
        coordinator = get_object_or_404(
            Coordinator,
            pk=pk
        )
        product_coordinator_list = coordinator.product_coordinators.all()
        return render(
            request,
            'companyinfo2/coordinator_detail.html',
            {'coordinator': coordinator, 'product_coordinator_list': product_coordinator_list}
        )


class CoordinatorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CoordinatorForm
    model = Coordinator
    permission_required = 'companyinfo2.add_coordinator'


class CoordinatorUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CoordinatorForm
    model = Coordinator
    template_name = 'companyinfo2/coordinator_form_update.html'
    permission_required = 'companyinfo2.change_coordinator'


class CoordinatorDelete(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'companyinfo2.delete_coordinator'

    def get(self, request, pk):
        coordinator = self.get_object(pk)
        product_coordinators = coordinator.product_coordinators.all()
        if product_coordinators.count() > 0:
            return render(
                request,
                'companyinfo2/coordinator_refuse_delete.html',
                {'coordinator': coordinator,
                 'product_coordinators': product_coordinators,
                 }
            )
        else:
            return render(
                request,
                'companyinfo2/coordinator_confirm_delete.html',
                {'coordinator': coordinator}
            )

    def get_object(self, pk):
        coordinator = get_object_or_404(
            Coordinator,
            pk=pk
        )
        return coordinator

    def post(self, request, pk):
        coordinator = self.get_object(pk)
        coordinator.delete()
        return redirect('companyinfo2_coordinator_list_urlpattern')


class Product_coordinatorList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product_coordinator
    permission_required = 'companyinfo2.view_product_coordinator'


class Product_coordinatorDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'companyinfo2.view_product_coordinator'

    def get(self, request, pk):
        product_coordinator = get_object_or_404(
            Product_coordinator,
            pk=pk
        )
        return render(
            request,
            'companyinfo2/product_coordinator_detail.html',
            {'product_coordinator': product_coordinator, 'coordinator': product_coordinator.coordinator,
             'product': product_coordinator.product}
        )


class Product_coordinatorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = Product_coordinatorForm
    model = Product_coordinator
    permission_required = 'companyinfo2.add_product_coordinator'


class Product_coordinatorUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = Product_coordinatorForm
    model = Product_coordinator
    template_name = 'companyinfo2/product_coordinator_form_update.html'
    permission_required = 'companyinfo2.change_product_coordinator'


class Product_coordinatorDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product_coordinator
    success_url = reverse_lazy('companyinfo2_product_coordinator_list_urlpattern')
    permission_required = 'companyinfo2.delete_product_coordinator'

    def get(self, request, pk):
        product_coordinator = self.get_object(pk)
        return render(
            request,
            'companyinfo2/product_coordinator_confirm_delete.html',
            {'product_coordinator': product_coordinator}
        )
    
    def get_object(self, pk):
        coordinator = get_object_or_404(
            Product_coordinator,
            pk=pk
        )
        return coordinator
    
    def post(self, request, pk):
        product_coordinator = self.get_object(pk)
        product_coordinator.delete()
        return redirect('companyinfo2_product_coordinator_list_urlpattern')
