# Generated by Django 5.1.3 on 2024-11-28 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenditure_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='credit_reform',
            field=models.CharField(choices=[('ΕΓΚΕΚΡΙΜΕΝΗ', 'ΕΓΚΕΚΡΙΜΕΝΗ'), ('ΑΝΑΜΟΡΦΩΣΗ', 'ΑΝΑΜΟΡΦΩΣΗ'), ('ΜΕΤΑΦΟΡΑ ΣΕ ΑΛΛΟ ΑΛΕ', 'ΜΕΤΑΦΟΡΑ ΣΕ ΑΛΛΟ ΑΛΕ'), ('ΑΠΟ ΜΕΤΑΦΟΡΑ', 'ΑΠΟ ΜΕΤΑΦΟΡΑ')], default='ΑΝΑΜΟΡΦΩΣΗ', max_length=100, verbose_name='Τύπος Πίστωσης'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='transfer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='expenditure_register.transfer', verbose_name='Μεταφορά'),
        ),
    ]
