# Generated by Django 4.0.5 on 2022-09-27 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenditure_register', '0023_alter_recall_diavgeia_string_alter_recall_recall_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforpaymentorinvoice',
            name='computed_payment_due_date',
            field=models.DateField(blank=True, default='', verbose_name='Ημερομηνία λήξης προθεσμίας υποχρέωσης (Μόνο για εμπορικές συναλλαγές)'),
        ),
        migrations.AlterField(
            model_name='requestforpaymentorinvoice',
            name='service_acceptance_verification_date',
            field=models.DateField(blank=True, default='', verbose_name='Ημερομηνία έγκρισης παραλαβής αγαθών, υπηρεσιών ή εργασιών (Μόνο για εμπορικές συναλλαγές)'),
        ),
        migrations.AlterField(
            model_name='requestforpaymentorinvoice',
            name='service_reception_date',
            field=models.DateField(blank=True, default='', verbose_name='Ημερομηνία παραλαβής αγαθών, υπηρεσιών ή εργασιών (Μόνο για εμπορικές συναλλαγές)'),
        ),
    ]
