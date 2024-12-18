# Generated by Django 4.2.16 on 2024-11-11 08:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
        ('hotline', '0008_alter_hotline_updated_by'),
        ('maintenance', '0007_alter_maintenance_anomaly_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maintenance',
            old_name='designation',
            new_name='diagnostic',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='anomaly',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='serialNumber',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='source',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='ticket',
        ),
        migrations.AddField(
            model_name='maintenance',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maintenance',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='hotline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotline.hotline'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='updated_by',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='status.status'),
        ),
    ]
