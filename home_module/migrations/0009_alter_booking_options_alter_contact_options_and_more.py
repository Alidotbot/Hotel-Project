# Generated by Django 4.1.5 on 2023-02-06 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0008_alter_booking_end_date_alter_booking_room_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'رزرو', 'verbose_name_plural': 'لیست رزرو ها'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'تماس با ما', 'verbose_name_plural': 'لیست تماس با ما'},
        ),
        migrations.AlterModelOptions(
            name='rooms',
            options={'verbose_name': 'اتاق', 'verbose_name_plural': 'اتاق ها'},
        ),
    ]