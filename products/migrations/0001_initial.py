# Generated by Django 4.0.3 on 2022-03-16 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to=' photos/%y/%m/%d')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]