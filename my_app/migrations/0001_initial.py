# Generated by Django 3.2 on 2022-03-25 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('max_employees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=6)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=20)),
                ('birthdate', models.DateField()),
                ('status', models.CharField(choices=[('Working', 'Работает'), ('Fired', 'Уволен'), ('Maternity leave', 'Декретный отпуск')], default='Работает', max_length=50)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.position')),
            ],
        ),
    ]