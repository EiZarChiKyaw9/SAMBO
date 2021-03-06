# Generated by Django 3.2.5 on 2021-07-17 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0004_alter_site_fu_site_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='wv_daily_report_details',
            name='FU_WV_Image',
            field=models.ImageField(blank=True, null=True, upload_to='wv_images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='site',
            name='FU_Site_Image',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d/'),
        ),
    ]
