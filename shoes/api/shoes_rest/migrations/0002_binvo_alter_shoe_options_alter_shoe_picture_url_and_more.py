# Generated by Django 4.0.3 on 2022-12-03 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BinVO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closet_name', models.CharField(max_length=100)),
                ('bin_number', models.PositiveSmallIntegerField()),
                ('bin_size', models.PositiveIntegerField()),
                ('import_href', models.CharField(max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='shoe',
            options={},
        ),
        migrations.AlterField(
            model_name='shoe',
            name='picture_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='bin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bins', to='shoes_rest.binvo'),
        ),
        migrations.DeleteModel(
            name='Bin',
        ),
    ]
