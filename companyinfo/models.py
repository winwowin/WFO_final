from django.db import models
from django.urls import reverse


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.supplier_name

    class Meta:
        ordering = ['supplier_name']


class Part(models.Model):
    part_id = models.AutoField(primary_key=True)
    part_number = models.CharField(max_length=20)
    part_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.part_number, self.part_name)

    class Meta:
        ordering = ['part_number', 'part_name']
        unique_together = (('part_number', 'part_name'),)


class Assembling(models.Model):
    assembling_id = models.AutoField(primary_key=True)
    assembling_code = models.CharField(max_length=45)
    assembling_line = models.CharField(max_length=45)

    def __str__(self):
        return '%s - %s - %s' % (self.assembling_id, self.assembling_code, self.assembling_line)

    class Meta:
        ordering = ['assembling_code', 'assembling_line']
        # unique_together = (('assembling_id', 'assembling_code', 'assembling_line'),)


class Coordinator(models.Model):
    coordinator_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    nickname = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.nickname == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.nickname)
        return result

    class Meta:
        ordering = ['last_name', 'first_name', 'nickname']
        unique_together = (('last_name', 'first_name', 'nickname'),)


# class Product(models.Model):
#     product_id = models.AutoField(primary_key=True)
#     product_name = models.CharField(max_length=45)
#     supplier = models.ForeignKey(Supplier, related_name='product', on_delete=models.PROTECT)
#     part = models.ForeignKey(Part, related_name='product', on_delete=models.PROTECT)
#     assembling = models.ForeignKey(Assembling, related_name='product', on_delete=models.PROTECT)
#
#     def __str__(self):
#         return '%s (%s) : %s' % (self.product_name, self.supplier.supplier_name, self.part)
#
#     class Meta:
#         ordering = ('product_name', 'supplier__supplier_name',)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=10)
    supplier = models.ForeignKey(Supplier, related_name='product', on_delete=models.PROTECT)
    part = models.ForeignKey(Part, related_name='product', on_delete=models.PROTECT,null=True)
    # assembling = models.ForeignKey(Assembling, related_name='product', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s (%s)' % (self.part.part_number, self.product_name, self.supplier.supplier_name)

    class Meta:
        ordering = ['part__part_number', 'product_name', 'supplier__supplier_name']


class Product_coordinator(models.Model):
    Liable_id = models.AutoField(primary_key=True)
    coordinator = models.ForeignKey(Coordinator, related_name='coordinator',  on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='product',  on_delete=models.PROTECT)

    def __str__(self):
        return '%s : %s' % (self.product, self.coordinator)

    class Meta:
        ordering = ['product', 'coordinator']
        unique_together = (('product', 'coordinator'),)
