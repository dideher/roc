# Generated by Django 4.0.5 on 2022-09-07 07:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expenditure_register', '0021_alter_payment_invoice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='balance',
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_amount_to_third_persons',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Συνολικό ποσό πληρωμής ληξιπρόθεσμων οφειλών > 90 ημερών προς τρίτους'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_type_choice',
            field=models.CharField(choices=[('ΕΞΟΦΛΗΣΗ', 'ΕΞΟΦΛΗΣΗ'), ('ΑΠΟΡΡΙΨΗ', 'ΑΠΟΡΡΙΨΗ'), ('ΑΚΥΡΩΣΗ', 'ΑΚΥΡΩΣΗ')], default='ΑΠΟΔΟΧΗ', max_length=100, verbose_name='Διαχείριση πληρωμής τιμολογίου ή ισοδύναμου εγγράφου'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='setoff_payment_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Εκ του οποίου συμψηφισμοί/παρακράτηση υπέρ Δημοσίου ή ΟΚΑ'),
        ),
        migrations.AlterField(
            model_name='requestforpaymentorinvoice',
            name='computed_maturation_start_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 8, 7, 53, 41, 153378, tzinfo=utc), verbose_name='Ημερομηνία έναρξης ωρίμανσης'),
        ),
        migrations.AlterField(
            model_name='requestforpaymentorinvoice',
            name='computed_payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 8, 7, 53, 41, 153399, tzinfo=utc), verbose_name='Ημερομηνία δημιουργίας υποχρέωσης'),
        ),
        migrations.AlterField(
            model_name='requestforpaymentorinvoice',
            name='payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 7, 7, 53, 41, 153340, tzinfo=utc), verbose_name='Ημερομηνία λήξης προθεσμίας πληρωμής'),
        ),
        migrations.CreateModel(
            name='Recall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recall', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ποσό Δέσμευσης')),
                ('recall_protocol_number', models.CharField(max_length=10, verbose_name='Αριθμός πρωτ. απόφασης ανάληψης υποχρέωσης')),
                ('recall_date', models.DateField(default=django.utils.timezone.now, verbose_name='Ημερομηνία Ανάληψης Υποχρέωσης')),
                ('diavgeia_string', models.CharField(max_length=100, verbose_name='ΑΔΑ')),
                ('diavgeia_date', models.DateField(default=django.utils.timezone.now, verbose_name='Ημερομηνία Ανάρτησης στη Διαύγεια')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenditure_register.account', verbose_name='ΑΛΕ')),
            ],
        ),
    ]
