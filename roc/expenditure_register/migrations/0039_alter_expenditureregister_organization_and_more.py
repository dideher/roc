# Generated by Django 4.0.5 on 2022-10-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenditure_register', '0038_requestforpaymentorinvoice_invoice_created_by_us_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenditureregister',
            name='organization',
            field=models.CharField(default='1019', max_length=20, verbose_name='Φορέας'),
        ),
        migrations.AlterField(
            model_name='expenditureregister',
            name='special_organization',
            field=models.CharField(default='206-9922000', max_length=20, verbose_name='Ειδικός Φορέας'),
        ),
        migrations.AlterField(
            model_name='requestforpaymentorinvoice',
            name='invoice_created_by_us',
            field=models.BooleanField(default=False, verbose_name='Αυτόματη συμπλήρωση υπόλοιπων ημερομηνιών (Μόνο αν το τιμολόγιο εκδόθηκε από το φορέα μας. Ελέγξτε τα αποτελέσματα!)'),
        ),
    ]
