# Generated by Django 4.1.7 on 2023-02-24 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessoriess',
            fields=[
                ('aid', models.CharField(default='', max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('price', models.FloatField(default=0.0)),
                ('net', models.IntegerField(default=0)),
                ('picture', models.ImageField(upload_to='static/IMGproduct/')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.CharField(default='', max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('location', models.CharField(default='', max_length=200)),
                ('tel', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('cgid', models.CharField(default='', max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('desc', models.TextField(default='', max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('name', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(default='', max_length=13)),
                ('birthdate', models.DateField(default=None)),
                ('address', models.TextField(default='', max_length=400)),
                ('tel', models.CharField(default='', max_length=10)),
                ('cid', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('postcode', models.CharField(default='', max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('name', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(default='', max_length=13)),
                ('position', models.CharField(default='', max_length=50)),
                ('birthdate', models.DateField(default=None)),
                ('address', models.TextField(default='', max_length=400)),
                ('tel', models.CharField(default='', max_length=50)),
                ('eid', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('branch', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('oid', models.CharField(default='', max_length=15, primary_key=True, serialize=False)),
                ('odate', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='', max_length=1)),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Transfers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdate', models.DateTimeField(auto_now_add=True)),
                ('reference', models.CharField(default='', max_length=35)),
                ('bank', models.CharField(default='', max_length=50)),
                ('bill', models.ImageField(default='', upload_to='static/bills/')),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Servise',
            fields=[
                ('odate', models.DateTimeField(auto_now_add=True)),
                ('person', models.TextField(default='', max_length=800)),
                ('type', models.CharField(default='', max_length=13)),
                ('weight', models.FloatField(default=0.0)),
                ('sid', models.CharField(default='', max_length=15, primary_key=True, serialize=False)),
                ('cus', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.customers')),
                ('s_start', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.district')),
            ],
        ),
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdate', models.DateTimeField(auto_now_add=True)),
                ('tag', models.CharField(default='', max_length=50)),
                ('barnch', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.branch')),
                ('employee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.employees')),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Samplesale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datesale', models.DateField(default=None)),
                ('amount', models.IntegerField(default=0)),
                ('accessories', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.accessoriess')),
            ],
        ),
        migrations.CreateModel(
            name='Reject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdate', models.DateTimeField(auto_now_add=True)),
                ('reason', models.CharField(default='', max_length=200)),
                ('employee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.employees')),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.orders')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oprice', models.FloatField(default=0.0)),
                ('quantity', models.IntegerField(default=1)),
                ('accessories', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.accessoriess')),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Confirms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(default='', max_length=200)),
                ('employee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.employees')),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Cancel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('reason', models.CharField(default='', max_length=200)),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.orders')),
            ],
        ),
        migrations.AddField(
            model_name='accessoriess',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.categories'),
        ),
        migrations.CreateModel(
            name='Accepts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adate', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.employees')),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Express.orders')),
            ],
        ),
    ]