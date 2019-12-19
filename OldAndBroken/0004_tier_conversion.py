
from __future__ import unicode_literals

from django.db import migrations, models
import re

YEARS = [
    {
        'year': 9999,
    },

]

TIER = [
    {
        "tier_level": 9999,
        "tier_name": "TemporaryValue",
    },
]


# def extract_year(supplier_name):
#     answer = re.findall(r'^\d{4} ', supplier_name)
#     if len(answer) != 1:
#         raise ValueError('Error found in year portion of supplier name:', supplier_name)
#     return answer[0]


def extract_tier_name(supplier_name):
    answer = re.findall(r' (PartSupplier|MaterialSupplier)$', supplier_name)
    if len(answer) != 1:
        raise ValueError('Error found in tier_level portion of supplier name:', supplier_name)
    return answer[0]


def forward_convert_supplier_data(apps, schema_editor):
    # year_class = apps.get_model('companyinfo2', 'Year')
    tier_class = apps.get_model('companyinfo2', 'Tier')
    supplier_class = apps.get_model('companyinfo2', 'Semester')

    suppliers = supplier_class.objects.all()
    for supplier in suppliers:
        # this_year = extract_year(supplier.supplier_name)
        this_tier_name = extract_tier_name(supplier.supplier_name)

        # year_object = year_class.objects.get(
        #     year=this_year
        # )
        # supplier.year = year_object
        # supplier.save()

        tier_object = tier_class.objects.get(
            tier_name=this_tier_name
        )
        supplier.tier = tier_object
        supplier.save()


def reverse_convert_supplier_data(apps, schema_editor):
    # year_class = apps.get_model('companyinfo2', 'Year')
    tier_class = apps.get_model('companyinfo2', 'Tier')
    supplier_class = apps.get_model('companyinfo2', 'Semester')

    suppliers = supplier_class.objects.all()
    for supplier in suppliers:
        supplier.supplier_name = supplier.tier.tier_name + ' - ' + str(supplier.supplier_name)
        #
        # year_object = year_class.objects.get(
        #     year=9999
        # )
        # supplier.year = year_object
        # supplier.save()

        tier_object = tier_class.objects.get(
            tier_level=9999
        )
        supplier.tier = tier_object
        supplier.save()


def remove_tier_level_data(apps, schema_editor):
    tier_class = apps.get_model('companyinfo2', 'Tier')
    for this_tier in TIER:
        tier_object = tier_class.objects.get(
            tier_level=this_tier['tier_level']
        )
        tier_object.delete()


def add_tier_level_data(apps, schema_editor):
    tier_class = apps.get_model('companyinfo2', 'Tier')
    for this_tier in TIER:
        tier_object = tier_class.objects.create(
            tier_level=this_tier['tier_level'],
            tier_name=this_tier['tier_name']
        )

#
# def remove_year_data(apps, schema_editor):
#     year_model_class = apps.get_model('companyinfo2', 'Year')
#     for this_year in YEARS:
#         year_object = year_model_class.objects.get(
#             year=this_year['year']
#         )
#         year_object.delete()
#
#
# def add_year_data(apps, schema_editor):
#     year_model_class = apps.get_model('companyinfo2', 'Year')
#     for this_year in YEARS:
#         year_object = year_model_class.objects.create(
#             year=this_year['year']
#         )

class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo2', '0003_tier'),
    ]

    operations = [

        migrations.AlterField(
            model_name='supplier',
            name='supplier_name',
            field=models.CharField(max_length=45, unique=False, default='temporary value'),
        ),

        # migrations.AddField(
        #     model_name='supplier',
        #     name='year',
        #     field=models.ForeignKey(to='companyinfo2.year', on_delete=models.PROTECT, default=1)
        # ),

        migrations.AddField(
            model_name='supplier',
            name='tier',
            field=models.ForeignKey(to='companyinfo2.tier', on_delete=models.PROTECT, default=9999)
        ),

        migrations.RunPython(
            forward_convert_supplier_data,
            reverse_convert_supplier_data
        ),

        migrations.RunPython(
            remove_tier_level_data,
            add_tier_level_data
        ),

        # migrations.RunPython(
        #     remove_year_data,
        #     add_year_data
        # ),

        migrations.RemoveField(
            model_name='supplier',
            name='supplier_name'
        ),

        # migrations.AlterField(
        #     model_name='supplier',
        #     name='year',
        #     field=models.ForeignKey(to='companyinfo2.year', on_delete=models.PROTECT)
        # ),

        migrations.AlterField(
            model_name='supplier',
            name='tier',
            field=models.ForeignKey(to='companyinfo2.tier', on_delete=models.PROTECT)
        ),

        migrations.AlterUniqueTogether(
            name="supplier",
            unique_together=set([('tier', 'supplier_name')]),
        ),


    ]
