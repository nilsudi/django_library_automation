# Generated by Django 4.2.6 on 2024-01-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
