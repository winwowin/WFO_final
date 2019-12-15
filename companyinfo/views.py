from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader

from .models import (Supplier, Product, Part, Assembling, Product_coordinator, Coordinator)


def assembling_list_view(request):
    assembling_list = Assembling.objects.all()
    # assembling_list = Assembling.objects.none()
    template = loader.get_template(
        'companyinfo/assembling_list.html')
    context = {'assembling_list': assembling_list}
    output = template.render(context)
    return HttpResponse(output)


def product_list_view(request):
    product_list = Product.objects.all()
    # product_list = Product.objects.none()
    template = loader.get_template(
        'companyinfo/product_list.html')
    context = {'product_list': product_list}
    output = template.render(context)
    return HttpResponse(output)


def part_list_view(request):
    part_list = Part.objects.all()
    # part_list = Part.objects.none()
    template = loader.get_template(
        'companyinfo/part_list.html')
    context = {'part_list': part_list}
    output = template.render(context)
    return HttpResponse(output)


def supplier_list_view(request):
    supplier_list = Supplier.objects.all()
    # supplier_list = Supplier.objects.none()
    template = loader.get_template(
        'companyinfo/supplier_list.html')
    context = {'supplier_list': supplier_list}
    output = template.render(context)
    return HttpResponse(output)


def coordinator_list_view(request):
    coordinator_list = Coordinator.objects.all()
    # coordinator_list = Coordinator.objects.none()
    template = loader.get_template(
        'companyinfo/coordinator_list.html')
    context = {'coordinator_list': coordinator_list}
    output = template.render(context)
    return HttpResponse(output)


def product_coordinator_list_view(request):
    product_coordinator_list = Product_coordinator.objects.all()
    # product_coordinator_list = Product_coordinator.objects.none()
    template = loader.get_template(
        'companyinfo/product_coordinator_list.html')
    context = {'product_coordinator_list': product_coordinator_list}
    output = template.render(context)
    return HttpResponse(output)
