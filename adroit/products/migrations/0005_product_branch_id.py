# Generated by Django 3.1 on 2020-11-12 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0002_auto_20201112_0032'),
        ('products', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='branch_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='branches.branch'),
        ),
    ]
