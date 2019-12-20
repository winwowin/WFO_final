from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.template import loader

from companyinfo2.utils import ObjectCreateMixin
from .models import (Supplier, Product, Part, Assembling, Product_coordinator, Coordinator)


from django.shortcuts import render, get_object_or_404, render_to_response
from django.views import View

from companyinfo2.forms import AssemblingForm, ProductForm, PartForm, SupplierForm, CoordinatorForm, Product_coordinatorForm


from .models import (
    Assembling,
    Product,
    Part,
    Supplier,
    Coordinator,
    Product_coordinator,
)


class AssemblingList(View):

    def get(self, request):
        return render(
            request,
            'companyinfo/assembling_list.html',
            {'assembling_list': Assembling.objects.all()}
        )


class AssemblingDetail(View):

    def get(self, request, pk):
        assembling = get_object_or_404(
            Assembling,
            pk=pk
        )
        product_list = assembling.products.all()
        return render(
            request,
            'companyinfo/assembling_detail.html',
            {'assembling': assembling, 'product_list': product_list}
        )


# class AssemblingCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
class AssemblingCreate(ObjectCreateMixin, View):
    form_class = AssemblingForm
    template_name = 'companyinfo2/assembling_form.html'
    # model = Assembling
    # permission_required = 'companyinfo2.add_assembling'


class ProductList(View):
# class ProductList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
#     model = Product
#     permission_required = 'companyinfo2.view_product'
    def get(self, request):
        return render(
            request,
            'companyinfo/product_list.html',
            {'product_list': Product.objects.all()}
        )


class ProductDetail(View):
# class ProductDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
#     permission_required = 'companyinfo2.view_product'
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
            'companyinfo/product_detail.html',
            {'product': product,
             'supplier': supplier,
             'part': part,
             'assembling': assembling,
             'product_coordinator_list': product_coordinator_list}
        )


# class ProductCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
class ProductCreate(ObjectCreateMixin, View):
    form_class = ProductForm
    template_name = 'companyinfo2/product_form.html'
    #
    # model = Product
    # permission_required = 'companyinfo2.add_product'


# class ProductUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
#     form_class = ProductForm
#     model = Product
#     template_name = 'companyinfo2/product_form_update.html'
#     permission_required = 'companyinfo2.change_product'

class ProductUpdate(View):
    form_class = ProductForm
    model = Product
    template_name = 'companyinfo2/product_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=product),
            'product': product,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        product = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=product)
        if bound_form.is_valid():
            new_product = bound_form.save()
            return redirect(new_product)
        else:
            context = {
                'form': bound_form,
                'product': product,
            }
            return render(
                request,
                self.template_name,
                context)


class ProductDelete(View):
# class ProductDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
#     permission_required = 'companyinfo2.delete_product'

    def get(self, request, pk):
        product = self.get_object(pk)
        product_coordinators = product.product_coordinators.all()
        if product_coordinators.count() > 0:
            return render(
                request,
                'companyinfo/product_refuse_delete.html',
                {'product': product,
                 'product_coordinators': product_coordinators,
                 }
            )
        else:
            return render(
                request,
                'companyinfo/product_confirm_delete.html',
                {'product': product}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Product,
            pk=pk)

    def post(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return redirect('companyinfo_product_list_urlpattern')




class PartList(View):
# class PartList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
#     model = Part
#     permission_required = 'companyinfo2.view_part'
    def get(self, request):
        return render(
            request,
            'companyinfo/part_list.html',
            {'part_list': Part.objects.all()}
        )


class PartDetail(View):
# class PartDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
#     permission_required = 'companyinfo2.view_part'
    def get(self, request, pk):
        part = get_object_or_404(
            Part,
            pk=pk
        )
        product_list = part.products.all()
        return render(
            request,
            'companyinfo/part_detail.html',
            {'part': part, 'product_list': product_list}
        )


# class PartCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
class PartCreate(ObjectCreateMixin, View):
    form_class = PartForm
    template_name = 'companyinfo2/part_form.html'
    # model = Part
    # permission_required = 'companyinfo2.add_part'


class PartUpdate(View):
# class PartUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = PartForm
    model = Part
    template_name = 'companyinfo2/part_form_update.html'
    # permission_required = 'companyinfo2.change_part'

    
    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)
    
    
    def get(self, request, pk):
        part = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=part),
            'part': part,
        }
        return render(
            request, self.template_name, context)
    
    
    def post(self, request, pk):
        part = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=part)
        if bound_form.is_valid():
            new_part = bound_form.save()
            return redirect(new_part)
        else:
            context = {
                'form': bound_form,
                'part': part,
            }
            return render(
                request,
                self.template_name,
                context)

class PartDelete(View):
# class PartDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
#     permission_required = 'companyinfo2.delete_part'

    def get(self, request, pk):
        part = self.get_object(pk)
        products = part.products.all()
        if products.count() > 0:
            return render(
                request,
                'companyinfo/part_refuse_delete.html',
                {'part': part,
                 'products': products,
                 }
            )
        else:
            return render(
                request,
                'companyinfo/part_confirm_delete.html',
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
        return redirect('companyinfo_part_list_urlpattern')



class SupplierList(View):
# class SupplierList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
#     model = Supplier
#     permission_required = 'companyinfo2.view_supplier'
    def get(self, request):
        return render(
            request,
            'companyinfo/supplier_list.html',
            {'supplier_list': Supplier.objects.all()}
        )


class SupplierDetail(View):
# class SupplierDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
#     permission_required = 'companyinfo2.view_supplier'
    def get(self, request, pk):
        supplier = get_object_or_404(
            Supplier,
            pk=pk
        )
        product_list = supplier.products.all()
        return render(
            request,
            'companyinfo/supplier_detail.html',
            {'supplier': supplier, 'product_list': product_list}
        )


# class SupplierCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
class SupplierCreate(ObjectCreateMixin, View):
    form_class = SupplierForm
    template_name = 'companyinfo2/supplier_form.html'

    # model = Supplier
    # permission_required = 'companyinfo2.add_supplier'


# class SupplierUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
#     form_class = SupplierForm
#     model = Supplier
#     template_name = 'companyinfo2/supplier_form_update.html'
#     permission_required = 'companyinfo2.change_supplier'

class SupplierUpdate(View):
    form_class = SupplierForm
    model = Supplier
    template_name = 'companyinfo2/supplier_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        supplier = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=supplier),
            'supplier': supplier,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        supplier = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=supplier)
        if bound_form.is_valid():
            new_supplier = bound_form.save()
            return redirect(new_supplier)
        else:
            context = {
                'form': bound_form,
                'supplier': supplier,
            }
            return render(
                request,
                self.template_name,
                context)
        

class SupplierDelete(View):
# class SupplierDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'companyinfo2.delete_supplier'

    def get(self, request, pk):
        supplier = self.get_object(pk)
        products = supplier.products.all()
        if products.count() > 0:
            return render(
                request,
                'companyinfo/supplier_refuse_delete.html',
                {'supplier': supplier,
                 'products': products,
                 }
            )
        else:
            return render(
                request,
                'companyinfo/supplier_confirm_delete.html',
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
        return redirect('companyinfo_supplier_list_urlpattern')



class CoordinatorList(View):
# class CoordinatorList(LoginRequiredMixin,PermissionRequiredMixin,PageLinksMixin, ListView):
#     paginate_by = 25
#     model = Coordinator
#     permission_required = 'companyinfo2.view_coordinator'
    def get(self, request):
        return render(
            request,
            'companyinfo/coordinator_list.html',
            {'coordinator_list': Coordinator.objects.all()}
        )


class CoordinatorDetail(View):
# class CoordinatorDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
#     permission_required = 'companyinfo2.view_coordinator'
    def get(self, request, pk):
        coordinator = get_object_or_404(
            Coordinator,
            pk=pk
        )
        product_coordinator_list = coordinator.product_coordinators.all()
        return render(
            request,
            'companyinfo/coordinator_detail.html',
            {'coordinator': coordinator, 'product_coordinator_list': product_coordinator_list}
        )


# class CoordinatorCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
class CoordinatorCreate(ObjectCreateMixin, View):
    form_class = CoordinatorForm
    template_name = 'companyinfo2/coordinator_form.html'

    # model = Coordinator
    # permission_required = 'companyinfo2.add_coordinator'


class CoordinatorUpdate(View):
# class CoordinatorUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = CoordinatorForm
    model = Coordinator
    template_name = 'companyinfo2/coordinator_form_update.html'
    # permission_required = 'companyinfo2.change_coordinator'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)
    
    def get(self, request, pk):
        coordinator = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=coordinator),
            'coordinator': coordinator,
        }
        return render(
            request, self.template_name, context)
    
    def post(self, request, pk):
        coordinator = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=coordinator)
        if bound_form.is_valid():
            new_coordinator = bound_form.save()
            return redirect(new_coordinator)
        else:
            context = {
                'form': bound_form,
                'coordinator': coordinator,
            }
            return render(
                request,
                self.template_name,
                context)


class CoordinatorDelete(View):
# class CoordinatorDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
#     permission_required = 'companyinfo2.delete_coordinator'

    def get(self, request, pk):
        coordinator = self.get_object(pk)
        product_coordinators = coordinator.product_coordinators.all()
        if product_coordinators.count() > 0:
            return render(
                request,
                'companyinfo/coordinator_refuse_delete.html',
                {'coordinator': coordinator,
                 'product_coordinators': product_coordinators,
                 }
            )
        else:
            return render(
                request,
                'companyinfo/coordinator_confirm_delete.html',
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
        return redirect('companyinfo_coordinator_list_urlpattern')


class Product_coordinatorList(View):
# class Product_coordinatorList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
#     model = Product_coordinator
#     permission_required = 'companyinfo2.view_product_coordinator'
    def get(self, request):
        return render(
            request,
            'companyinfo/product_coordinator_list.html',
            {'product_coordinator_list': Product_coordinator.objects.all()}
        )


class Product_coordinatorDetail(View):
# class Product_coordinatorDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
#     permission_required = 'companyinfo2.view_product_coordinator'
    def get(self, request, pk):
        product_coordinator = get_object_or_404(
            Product_coordinator,
            pk=pk
        )
        return render(
            request,
            'companyinfo/product_coordinator_detail.html',
            {'product_coordinator': product_coordinator, 'coordinator': product_coordinator.coordinator, 'product': product_coordinator.product}
        )


# class Product_coordinatorCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
class Product_coordinatorCreate(ObjectCreateMixin, View):
    form_class = Product_coordinatorForm
    template_name = 'companyinfo2/product_coordinator_form.html'

    # model = Product_coordinator
    # permission_required = 'companyinfo2.add_product_coordinator'

#
class Product_coordinatorUpdate(View):
# class Product_coordinatorUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = Product_coordinatorForm
    model = Product_coordinator
    template_name = 'companyinfo2/product_coordinator_form_update.html'
    # permission_required = 'companyinfo2.change_product_coordinator'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        product_coordinator = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=product_coordinator),
            'product_coordinator': product_coordinator,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        product_coordinator = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=product_coordinator)
        if bound_form.is_valid():
            new_product_coordinator = bound_form.save()
            return redirect(new_product_coordinator)
        else:
            context = {
                'form': bound_form,
                'product_coordinator': product_coordinator,
            }
            return render(
                request,
                self.template_name,
                context)


class Product_coordinatorDelete(View):
# class Product_coordinatorDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
#     model = Product_coordinator
#     success_url = reverse_lazy('companyinfo_product_coordinator_list_urlpattern')
#     permission_required = 'companyinfo2.delete_product_coordinator'

    def get(self, request, pk):
        product_coordinator = self.get_object(pk)
        return render(
            request,
            'companyinfo/product_coordinator_confirm_delete.html',
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
        return redirect('companyinfo_product_coordinator_list_urlpattern')














# 
# def assembling_list_view(request):
#     assembling_list = Assembling.objects.all()
#     # assembling_list = Assembling.objects.none()
#     template = loader.get_template(
#         'companyinfo2/assembling_list.html')
#     context = {'assembling_list': assembling_list}
#     output = template.render(context)
#     return HttpResponse(output)
# 
# 
# def product_list_view(request):
#     product_list = Product.objects.all()
#     # product_list = Product.objects.none()
#     template = loader.get_template(
#         'companyinfo2/product_list.html')
#     context = {'product_list': product_list}
#     output = template.render(context)
#     return HttpResponse(output)
# 
# 
# def part_list_view(request):
#     part_list = Part.objects.all()
#     # part_list = Part.objects.none()
#     template = loader.get_template(
#         'companyinfo2/part_list.html')
#     context = {'part_list': part_list}
#     output = template.render(context)
#     return HttpResponse(output)
# 
# 
# def supplier_list_view(request):
#     supplier_list = Supplier.objects.all()
#     # supplier_list = Supplier.objects.none()
#     template = loader.get_template(
#         'companyinfo2/supplier_list.html')
#     context = {'supplier_list': supplier_list}
#     output = template.render(context)
#     return HttpResponse(output)
# 
# 
# def coordinator_list_view(request):
#     coordinator_list = Coordinator.objects.all()
#     # coordinator_list = Coordinator.objects.none()
#     template = loader.get_template(
#         'companyinfo2/coordinator_list.html')
#     context = {'coordinator_list': coordinator_list}
#     output = template.render(context)
#     return HttpResponse(output)
# 
# 
# def product_coordinator_list_view(request):
#     product_coordinator_list = Product_coordinator.objects.all()
#     # product_coordinator_list = Product_coordinator.objects.none()
#     template = loader.get_template(
#         'companyinfo2/product_coordinator_list.html')
#     context = {'product_coordinator_list': product_coordinator_list}
#     output = template.render(context)
#     return HttpResponse(output)























# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.shortcuts import render, get_object_or_404, redirect
# from django.urls import reverse_lazy
# from django.views import View
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#
# from companyinfo2.forms import AssemblingForm, ProductForm, PartForm, SupplierForm, CoordinatorForm, Product_coordinatorForm
# # from companyinfo2.utils import PageLinksMixin
# from .models import (
#     Assembling,
#     Product,
#     Part,
#     Supplier,
#     Coordinator,
#     Product_coordinator,
# )
#
#
# class AssemblingList(LoginRequiredMixin,PermissionRequiredMixin,PageLinksMixin, ListView):
#     paginate_by = 25
#     model = Assembling
#     permission_required = 'companyinfo2.view_assembling'
#
#
# class AssemblingDetail(LoginRequiredMixin,PermissionRequiredMixin,View):
#     permission_required = 'companyinfo2.view_assembling'
#
#     def get(self, request, pk):
#         assembling = get_object_or_404(
#             Assembling,
#             pk=pk
#         )
#         product_list = assembling.products.all()
#         return render(
#             request,
#             'companyinfo2/assembling_detail.html',
#             {'assembling': assembling, 'product_list': product_list}
#         )
#
#
# class AssemblingCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
#     form_class = AssemblingForm
#     model = Assembling
#     permission_required = 'companyinfo2.add_assembling'
#
#

class AssemblingUpdate(View):

# class AssemblingUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    form_class = AssemblingForm
    model = Assembling
    template_name = 'companyinfo2/assembling_form_update.html'
    # permission_required = 'companyinfo2.change_assembling'


    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)


    def get(self, request, pk):
        assembling = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=assembling),
            'assembling': assembling,
        }
        return render(
            request, self.template_name, context)


    def post(self, request, pk):
        assembling = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=assembling)
        if bound_form.is_valid():
            new_assembling = bound_form.save()
            return redirect(new_assembling)
        else:
            context = {
                'form': bound_form,
                'assembling': assembling,
            }
            return render(
                request,
                self.template_name,
                context)


class AssemblingDelete(View):

# class AssemblingDelete(LoginRequiredMixin,PermissionRequiredMixin,View):
#     permission_required = 'companyinfo2.delete_assembling'

    def get(self, request, pk):
        assembling = self.get_object(pk)
        products = assembling.products.all()
        if products.count() > 0:
            return render(
                request,
                'companyinfo/assembling_refuse_delete.html',
                {'assembling': assembling,
                 'products': products,
                 }
            )
        else:
            return render(
                request,
                'companyinfo/assembling_confirm_delete.html',
                {'assembling': assembling}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Assembling,
            pk=pk)

    def post(self, request, pk):
        assembling = self.get_object(pk)
        assembling.delete()
        return redirect('companyinfo_assembling_list_urlpattern')
