# Generated by Django 4.0.2 on 2022-02-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev_tools_app', '0004_alter_articles_link_alter_articles_uploaded_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='uploaded_by',
        ),
        migrations.RemoveField(
            model_name='books',
            name='link',
        ),
        migrations.RemoveField(
            model_name='books',
            name='uploaded_by',
        ),
        migrations.RemoveField(
            model_name='videos',
            name='uploaded_by',
        ),
        migrations.AddField(
            model_name='books',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='documents'),
        ),
    ]