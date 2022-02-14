# Generated by Django 4.0.2 on 2022-02-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_book_publish_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_status',
            field=models.CharField(choices=[('Published', 'Published'), ('Unpublished', 'Unpublished'), ('Unknown', 'Unknown')], max_length=12),
        ),
    ]