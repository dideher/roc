# Generated by Django 4.0.5 on 2022-09-27 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenditure_register', '0025_alter_requestforpaymentorinvoice_invoice_series_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforpaymentorinvoice',
            name='invoice_series',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Σειρά τιμολογίου ή άλλου φορολογικού στοιχείου'),
        ),
    ]
