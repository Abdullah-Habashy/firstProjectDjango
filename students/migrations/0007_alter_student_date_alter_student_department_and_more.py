# Generated by Django 4.0.3 on 2022-03-18 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('choice1', 'primary'), ('choice2', 'Preparatory'), ('choice3', 'Secondary')], default='hababshy', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(upload_to=' photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default='habashy', max_length=50),
        ),
    ]