# Generated by Django 4.1.5 on 2023-03-04 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0013_settingsite_header_is_main_setting_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingsite_header',
            name='address',
            field=models.CharField(default='cosabod', max_length=10000, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='settingsite_header',
            name='description',
            field=models.CharField(default='cos', max_length=1000, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='settingsite_header',
            name='title',
            field=models.CharField(max_length=3000, verbose_name='نام'),
        ),
    ]