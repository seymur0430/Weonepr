# Generated by Django 5.2.3 on 2025-06-19 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_customuser_price_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='price_type',
            field=models.CharField(default='qiymeti daxil edin', max_length=100),
        ),
    ]
