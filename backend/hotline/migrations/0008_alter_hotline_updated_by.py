# Generated by Django 4.2.16 on 2024-11-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0007_alter_hotline_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotline',
            name='updated_by',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
