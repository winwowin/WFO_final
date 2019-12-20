from django.db import models
from django.urls import reverse


class Assembling(models.Model):
    assembling_id = models.AutoField(primary_key=True)
    assembling_code = models.CharField(max_length=45)
    assembling_line = models.CharField(max_length=45)

    def __str__(self):
        return '%s, %s' % (self.assembling_code, self.assembling_line)

    def get_absolute_url(self):
        return reverse('companyinfo_assembling_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('companyinfo_assembling_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse(
            'companyinfo_assembling_delete_urlpattern',
            kwargs={'pk': self.pk}
        )

    class Meta:
        ordering = ['assembling_code', 'assembling_line']
        unique_together = (('assembling_code', 'assembling_line'),)


class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=45, unique=True)
    state_code = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return '%s - %s' % (self.state_code, self.state_name)

    class Meta:
        ordering = ['state_code', 'state_name']


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=45, unique=True)
    country_code = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return '%s - %s' % (self.country_code, self.country_name)

    class Meta:
        ordering = ['country_code', 'country_name']
        
        
class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address_name = models.CharField(max_length=45, unique=True)
    address_number = models.IntegerField(unique=False)
    street_name = models.CharField(max_length=45, unique=False)
    district_name = models.CharField(max_length=45, unique=False)
    city_name = models.CharField(max_length=45, unique=False)
    state = models.ForeignKey(State, related_name='addresses', on_delete=models.PROTECT)
    country = models.ForeignKey(Country, related_name='addresses', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.address_name, self.city_name, self.state, self.country)

    def get_absolute_url(self):
        return reverse('companyinfo_address_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('companyinfo_address_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('companyinfo_address_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['country', 'state', 'city_name', 'address_name']
        

class Tier(models.Model):
    tier_id = models.AutoField(primary_key=True)
    tier_level = models.IntegerField(unique=True)
    tier_name = models.CharField(max_length=45,unique=True)

    def __str__(self):
        return '%s - %s' % (self.tier_level, self.tier_name)

    class Meta:
        ordering = ['tier_level']


# Attempt to create tier failed.

# class Supplier(models.Model):
#     supplier_id = models.AutoField(primary_key=True)
#     supplier_name = models.CharField(max_length=45, unique=True)
#     tier = models.ForeignKey(Tier, related_name='suppliers', on_delete=models.PROTECT)
#     address = models.ForeignKey(Address, related_name='suppliers', on_delete=models.PROTECT)
#
#     def __str__(self):
#         return '%s - %s' % (self.tier, self.supplier_name, self.address)
#
#     def get_absolute_url(self):
#         return reverse('companyinfo_supplier_detail_urlpattern',
#                        kwargs={'pk': self.pk})
#
#     def get_update_url(self):
#         return reverse('companyinfo_supplier_update_urlpattern',
#                        kwargs={'pk': self.pk}
#                        )
#
#     def get_delete_url(self):
#         return reverse('companyinfo_supplier_delete_urlpattern',
#                        kwargs={'pk': self.pk}
#                        )
#
#     class Meta:
#         ordering = ['tier__tier_level', 'supplier_name', 'address']


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.supplier_name

    def get_absolute_url(self):
        return reverse('companyinfo_supplier_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('companyinfo_supplier_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('companyinfo_supplier_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['supplier_name']


class Part(models.Model):
    part_id = models.AutoField(primary_key=True)
    part_number = models.CharField(max_length=20)
    part_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.part_number, self.part_name)

    def get_absolute_url(self):
        return reverse('companyinfo_part_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('companyinfo_part_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('companyinfo_part_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['part_number', 'part_name']
        unique_together = (('part_number', 'part_name'),)


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

    def get_absolute_url(self):
        return reverse('companyinfo_coordinator_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('companyinfo_coordinator_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('companyinfo_coordinator_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['last_name', 'first_name', 'nickname']
        unique_together = (('last_name', 'first_name', 'nickname'),)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=10)
    supplier = models.ForeignKey(Supplier, related_name='products', on_delete=models.PROTECT)
    part = models.ForeignKey(Part, related_name='products', on_delete=models.PROTECT)
    assembling = models.ForeignKey(Assembling, related_name='products', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s (%s)' % (self.part.part_number, self.product_name, self.supplier.__str__())

    def get_absolute_url(self):
        return reverse('companyinfo_product_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('companyinfo_product_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('companyinfo_product_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['part__part_number', 'product_name', 'supplier__supplier_name']
        unique_together = (('supplier', 'part', 'product_name'),)


class Product_coordinator(models.Model):
    product_coordinator_id = models.AutoField(primary_key=True)
    coordinator = models.ForeignKey(Coordinator, related_name='product_coordinators',  on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='product_coordinators',  on_delete=models.PROTECT)

    def __str__(self):
        return '%s / %s' % (self.product, self.coordinator)

    def get_absolute_url(self):
        return reverse('companyinfo_product_coordinator_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('companyinfo_product_coordinator_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('companyinfo_product_coordinator_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['product', 'coordinator']
        unique_together = (('product', 'coordinator'),)


class Billing(models.Model):
    billing_id = models.AutoField(primary_key=True)
    billing_number = models.IntegerField(unique=True)
    billing_name = models.CharField(max_length=45, unique=True)
    supplier = models.ForeignKey(Supplier, related_name='billings', on_delete=models.PROTECT)
    address = models.ForeignKey(Address, related_name='billings', on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s - %s' % (self.supplier.supplier_id, self.supplier.supplier_name, self.billing_number)

    def get_absolute_url(self):
        return reverse('companyinfo_billing_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('companyinfo_billing_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('companyinfo_billing_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['supplier__supplier_id', 'billing_number']
