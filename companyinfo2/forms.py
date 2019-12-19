from django import forms

from companyinfo2.models import Assembling, Product, Part, Supplier, Coordinator, Product_coordinator


class AssemblingForm(forms.ModelForm):
    class Meta:
        model = Assembling
        fields = '__all__'

    def clean_assembling_code(self):
        return self.cleaned_data['assembling_code'].strip()

    def clean_assembling_line(self):
        return self.cleaned_data['assembling_line'].strip()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_product_name(self):
        return self.cleaned_data['product_name'].strip()


class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = '__all__'

    def clean_part_number(self):
        return self.cleaned_data['part_number'].strip()

    def clean_part_name(self):
        return self.cleaned_data['part_name'].strip()


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

    def clean_supplier_name(self):
        return self.cleaned_data['supplier_name'].strip()


class CoordinatorForm(forms.ModelForm):
    class Meta:
        model = Coordinator
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_nickname(self):
        if len(self.cleaned_data['nickname']) == 0:
            result = self.cleaned_data['nickname']
        else:
            result = self.cleaned_data['nickname'].strip()
        return result


class Product_coordinatorForm(forms.ModelForm):
    class Meta:
        model = Product_coordinator
        fields = '__all__'
