# Generated by Django 4.0.6 on 2022-07-20 20:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('trak', '0009_alter_address_country'),
        ('accounts', '0002_alter_profile_epa_sites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='epa_sites',
            field=models.ManyToManyField(blank=True, null=True, related_name='sites',
                                         to='trak.site'),
        ),
    ]
