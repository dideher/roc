# Generated by Django 4.0.5 on 2022-07-14 10:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expenditure_register', '0019_rename_paymentdocument_payment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='request_for_payment',
            new_name='invoice',
        ),
        migrations.AlterField(
            model_name='requestforpaymentorinvoice',
            name='computed_maturation_start_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 15, 10, 50, 2, 864792, tzinfo=utc), verbose_name='Ημερομηνία έναρξης ωρίμανσης'),
        ),
        migrations.AlterField(
            model_name='requestforpaymentorinvoice',
            name='computed_payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 15, 10, 50, 2, 864807, tzinfo=utc), verbose_name='Ημερομηνία δημιουργίας υποχρέωσης'),
        ),
        migrations.AlterField(
            model_name='requestforpaymentorinvoice',
            name='payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 13, 10, 50, 2, 864758, tzinfo=utc), verbose_name='Ημερομηνία λήξης προθεσμίας πληρωμής'),
        ),
    ]
