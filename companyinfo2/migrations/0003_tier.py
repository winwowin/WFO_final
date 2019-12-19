# Generated by Django 2.2.1 on 2019-12-19 21:10

from django.db import migrations, models


TIER = [
    {
        "tier_level": 9999,
        "tier_name": "TemporaryValue",
    },
    {
        "tier_level": 1,
        "tier_name": "PartSupplier",
    },
    {
        "tier_level": 2,
        "tier_name": "MaterialSupplier",
    },

]


def add_tier_data(apps, schema_editor):
    tier_class = apps.get_model('companyinfo2', 'Tier')
    for this_tier in TIER:
        tier_object = tier_class.objects.create(
            tier_level=this_tier['tier_level'],
            tier_name=this_tier['tier_name']
        )


def remove_tier_data(apps, schema_editor):
    tier_class = apps.get_model('companyinfo2', 'Tier')
    for this_tier in TIER:
        tier_object = tier_class.objects.get(
            tier_level=this_tier['tier_level']
        )
        tier_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo2', '0002_auto_20191218_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('tier_id', models.AutoField(primary_key=True, serialize=False)),
                ('tier_level', models.IntegerField(unique=True)),
                ('tier_name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'ordering': ['tier_level'],
            },
        ),
        migrations.RunPython(
            add_tier_data,
            remove_tier_data
        )
    ]
