# Generated by Django 4.2.10 on 2024-02-16 19:21

import apps.manifest.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('handler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_mtn', models.JSONField(blank=True, help_text='Original manifest tracking number of rejected manifestRegex expression validation: [0-9]{9}[A-Z]{3}', null=True, validators=[apps.manifest.models.validate_mtn])),
                ('new_destination', models.CharField(blank=True, choices=[('GEN', 'Generator'), ('TSD', 'Tsdf')], help_text='Destination of the new manifest created during rejection or residue.', max_length=255, null=True)),
                ('consent_number', models.CharField(blank=True, max_length=12, null=True)),
                ('comments', models.JSONField(blank=True, null=True)),
                ('handling_instructions', models.CharField(blank=True, help_text='Special Handling Instructions', max_length=4000, null=True)),
            ],
            options={
                'verbose_name': 'Additional Info',
                'verbose_name_plural': 'Additional Info',
            },
        ),
        migrations.CreateModel(
            name='CorrectionInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(blank=True, null=True)),
                ('ppc_active', models.BooleanField(blank=True, null=True)),
                ('epa_site_id', models.CharField(blank=True, max_length=100, null=True)),
                ('initiator_role', models.CharField(blank=True, choices=[('IN', 'Industry'), ('PP', 'Ppc'), ('EP', 'Epa'), ('ST', 'State')], max_length=2, null=True)),
                ('update_role', models.CharField(blank=True, choices=[('IN', 'Industry'), ('PP', 'Ppc'), ('EP', 'Epa'), ('ST', 'State')], max_length=2, null=True)),
            ],
            options={
                'verbose_name': 'Correction Info',
                'verbose_name_plural': 'Correction Info',
            },
        ),
        migrations.CreateModel(
            name='PortOfEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, choices=[('AK', 'Alaska'), ('AL', 'Alabama'), ('AP', 'Armed Forces Pacific'), ('AR', 'Arkansas'), ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'Washington DC'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MO', 'Missouri'), ('MS', 'Mississippi'), ('MT', 'Montana'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('NY', 'New York'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VI', 'Virgin Islands'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming'), ('XA', 'REGION 01 PURVIEW'), ('XB', 'REGION 02 PURVIEW'), ('XC', 'REGION 03 PURVIEW'), ('XD', 'REGION 04 PURVIEW'), ('XE', 'REGION 05 PURVIEW'), ('XF', 'REGION 06 PURVIEW'), ('XG', 'REGION 07 PURVIEW'), ('XH', 'REGION 08 PURVIEW'), ('XI', 'REGION 09 PURVIEW'), ('XJ', 'REGION 10 PURVIEW')], max_length=2, null=True)),
                ('city_port', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Port of Entry',
                'verbose_name_plural': 'Ports of Entry',
            },
        ),
        migrations.CreateModel(
            name='Manifest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('mtn', models.CharField(default=apps.manifest.models.draft_mtn, max_length=30, unique=True, validators=[apps.manifest.models.validate_mtn], verbose_name='manifest Tracking Number')),
                ('status', models.CharField(choices=[('NotAssigned', 'Not Assigned'), ('Pending', 'Pending'), ('Scheduled', 'Scheduled'), ('InTransit', 'In Transit'), ('ReadyForSignature', 'Ready for Signature'), ('Signed', 'Signed'), ('Corrected', 'Corrected'), ('UnderCorrection', 'Under Correction'), ('MtnValidationFailed', 'MTN Validation Failed')], default='NotAssigned', max_length=25)),
                ('submission_type', models.CharField(choices=[('FullElectronic', 'Full Electronic'), ('DataImage5Copy', 'Data + Image'), ('Hybrid', 'Hybrid'), ('Image', 'Image')], default='FullElectronic', max_length=25)),
                ('signature_status', models.BooleanField(blank=True, null=True)),
                ('origin_type', models.CharField(choices=[('Web', 'Web'), ('Service', 'Service'), ('Mail', 'Mail')], default='Service', max_length=25)),
                ('shipped_date', models.DateTimeField(blank=True, null=True)),
                ('potential_ship_date', models.DateTimeField(blank=True, null=True, verbose_name='potential ship date')),
                ('received_date', models.DateTimeField(blank=True, null=True)),
                ('certified_date', models.DateTimeField(blank=True, null=True)),
                ('certified_by', models.JSONField(blank=True, null=True)),
                ('broker', models.JSONField(blank=True, null=True)),
                ('rejection', models.BooleanField(blank=True, null=True)),
                ('rejection_info', models.JSONField(blank=True, null=True, verbose_name='Rejection Information')),
                ('discrepancy', models.BooleanField(blank=True, default=False)),
                ('residue', models.BooleanField(blank=True, default=False)),
                ('residue_new_mtn', models.JSONField(blank=True, default=list, verbose_name='residue new MTN')),
                ('import_flag', models.BooleanField(blank=True, default=False, verbose_name='import')),
                ('import_info', models.JSONField(blank=True, null=True, verbose_name='import information')),
                ('contains_residue_or_rejection', models.BooleanField(blank=True, null=True, verbose_name='contains previous rejection or residue waste')),
                ('printed_document', models.JSONField(blank=True, null=True)),
                ('form_document', models.JSONField(blank=True, null=True)),
                ('correction_info', models.JSONField(blank=True, null=True)),
                ('ppc_status', models.JSONField(blank=True, null=True, verbose_name='PPC info')),
                ('locked', models.BooleanField(blank=True, null=True)),
                ('lock_reason', models.CharField(blank=True, choices=[('ACS', 'AsyncSign'), ('ECB', 'EpaChangeBiller'), ('EPC', 'EpaCorrection')], max_length=25, null=True)),
                ('transfer_requested', models.BooleanField(blank=True, null=True)),
                ('transfer_status', models.CharField(blank=True, max_length=200, null=True)),
                ('original_sub_type', models.CharField(blank=True, choices=[('FullElectronic', 'Full Electronic'), ('DataImage5Copy', 'Data + Image'), ('Hybrid', 'Hybrid'), ('Image', 'Image')], max_length=25, null=True, verbose_name='original submission type')),
                ('transfer_count', models.IntegerField(blank=True, null=True)),
                ('next_transfer_time', models.DateTimeField(blank=True, null=True, verbose_name='next transfer time')),
                ('additional_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manifest.additionalinfo')),
                ('generator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='generator', to='handler.handler')),
                ('tsdf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='designated_facility', to='handler.handler', verbose_name='designated facility')),
            ],
            options={
                'ordering': ['update_date', 'mtn'],
            },
        ),
        migrations.CreateModel(
            name='ImportInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_generator', models.JSONField(blank=True, null=True)),
                ('port_of_entry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='manifest.portofentry')),
            ],
            options={
                'verbose_name': 'Import Info',
                'verbose_name_plural': 'Import Info',
            },
        ),
    ]
