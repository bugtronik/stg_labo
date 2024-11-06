# Generated by Django 4.2.14 on 2024-11-06 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0001_initial'),
        ('locality', '0001_initial'),
        ('maintenance', '0004_alter_maintenance_locality_alter_maintenance_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='anomaly',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='date_sortie',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='locality.locality'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='observation',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='source.source'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='ticket',
            field=models.CharField(max_length=100),
        ),
    ]
