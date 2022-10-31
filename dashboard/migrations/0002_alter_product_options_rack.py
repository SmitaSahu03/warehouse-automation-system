# Generated by Django 4.0.6 on 2022-10-11 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product'},
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rack', models.CharField(max_length=100, null=True)),
                ('rack_quantity', models.PositiveIntegerField(null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.product')),
            ],
        ),
    ]
