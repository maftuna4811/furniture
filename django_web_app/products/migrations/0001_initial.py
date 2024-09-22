# Generated by Django 5.0.6 on 2024-06-19 03:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'category',
                'ordering': ['id'],
                'indexes': [models.Index(fields=['id'], name='category_id_db0083_idx')],
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'coupons',
                'ordering': ['id'],
                'indexes': [models.Index(fields=['id'], name='coupons_id_93c86d_idx')],
            },
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, null=True)),
                ('fullname', models.CharField(max_length=150)),
                ('chat_id', models.BigIntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'telegram_users',
                'ordering': ['id'],
                'indexes': [models.Index(fields=['id'], name='telegram_us_id_403e42_idx')],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_list', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pay_type', models.CharField(max_length=50)),
                ('pay_time', models.DateTimeField(auto_now_add=True)),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.coupon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'payments',
                'ordering': ['id'],
                'indexes': [models.Index(fields=['id'], name='payments_id_71f414_idx')],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='products/')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('count', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('endurance', models.IntegerField()),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'db_table': 'products',
                'ordering': ['id'],
                'indexes': [models.Index(fields=['id'], name='products_id_5ad420_idx')],
            },
        ),
    ]
