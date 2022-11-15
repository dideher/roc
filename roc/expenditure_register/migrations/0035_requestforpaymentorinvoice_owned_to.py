# Generated by Django 4.0.5 on 2022-09-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenditure_register', '0034_alter_payment_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestforpaymentorinvoice',
            name='owned_to',
            field=models.CharField(choices=[('ΤΡΙΤΟΥΣ', 'ΤΡΙΤΟΥΣ'), ('ΓΕΝΙΚΗ ΚΥΒΕΡΝΗΣΗ', 'ΓΕΝΙΚΗ ΚΥΒΕΡΝΗΣΗ')], default='ΤΡΙΤΟΥΣ', max_length=100, verbose_name='Υποχρέωση προς'),
        ),
    ]
